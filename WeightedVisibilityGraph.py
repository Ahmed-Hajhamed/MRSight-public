import numpy as np
import chemical_shifts
import bct
from HVG import horizontal_visibility_graph
from visibility_graph import visibility_graph

# Constants
MIN_THICKNESS = 1.2
MAX_THICKNESS = 4
MIN_ALPHA = 0.51
MAX_ALPHA = 1.0

# Load data
spectra = np.loadtxt('Datasets/spectra.csv', delimiter=',', dtype=np.float64)
chemical_shifts_array = np.loadtxt('Datasets/chemical_shifts.csv', delimiter=',', dtype=np.float64)
metabolite_shifts = chemical_shifts.chemical_shifts

class Graph:
    def __init__(self, subject_id, graph_type="Complete Metabolite Graph"):
        self.subject_index = subject_id
        self.graph_type = graph_type
        self.current_spectrum = spectra[:, subject_id]
        self.nodes = []
        self.edges = []
        self.indices = []
        self.initialize_graph()
        
    def initialize_graph(self):
        self.create_nodes()
        self.reduce_series()
        self.create_edges()
        self.normalize_weights()
        self.compute_graph_features()
        
    def change_graph_type(self, graph_type):
        self.graph_type = graph_type  
        self.initialize_graph()

    def change_subject(self, subject_id):
        self.subject_index = subject_id
        self.current_spectrum = spectra[:, subject_id]
        self.initialize_graph()

    def create_nodes(self):
        self.nodes = []
        pcr_intensity = 1.0  # Default value

        for details in metabolite_shifts.values():
            shift_value = details['value']
            symbol = details['symbol']
            index = np.argmin(np.abs(chemical_shifts_array - shift_value))
            intensity = self.current_spectrum[index]
            
            if symbol == 'PCr':
                pcr_intensity = intensity
                
            self.indices.append(index)
            self.nodes.append({"name": symbol, "coordinates": (shift_value, intensity)})

        # Sort and calculate PCr ratio
        self.nodes = sorted(self.nodes, key=lambda x: x['coordinates'][1], reverse=True)
        for node in self.nodes:
            node['pcr_ratio'] = node['coordinates'][1] / pcr_intensity
            
        # Initialize adjacency matrix
        n = len(self.nodes)
        self.undirected_connection_matrix = np.zeros((n, n), dtype=np.float64)

    def reduce_series(self):
        self.non_sorted_nodes = sorted(self.nodes.copy(), key=lambda x: x['coordinates'][0], reverse=True)
        self.reduced_series = [node["coordinates"][1] for node in self.non_sorted_nodes]

    def create_edges(self):
        self.edges = []
        
        if self.graph_type.lower() == "complete metabolite graph":
            for i in range(len(self.nodes)):
                for j in range(i + 1, len(self.nodes)):
                    self.add_edge(self.nodes[i], self.nodes[j], i, j)
        else:
            # Create visibility graph
            if self.graph_type.lower() == "natural visibility graph":
                graph = visibility_graph(self.reduced_series)
            elif self.graph_type.lower() == "horizontal visibility graph":
                graph = horizontal_visibility_graph(self.reduced_series)
                
            # Convert graph to edges
            for i, j in graph.edges():
                self.add_edge(self.non_sorted_nodes[i], self.non_sorted_nodes[j], i, j)

    def add_edge(self, metabolite_1, metabolite_2, i, j):
        edge, weight = self.construct_edge(metabolite_1, metabolite_2)
        self.undirected_connection_matrix[i, j] = weight
        self.undirected_connection_matrix[j, i] = 1 / weight
        self.edges.append(edge)

    def construct_edge(self, metabolite_1, metabolite_2):
        if metabolite_1["coordinates"][1] >= metabolite_2["coordinates"][1]:
            top, bottom = metabolite_1, metabolite_2
        else:
            top, bottom = metabolite_2, metabolite_1

        weight = top["coordinates"][1] / bottom["coordinates"][1]

        edge = {
            "source": top["name"],
            "target": bottom["name"],
            "weight": weight
        }
        return edge, weight

    def normalize_weights(self):
        if not self.edges:
            return
            
        weights = [abs(edge["weight"]) for edge in self.edges]
        self.min_w, self.max_w = min(weights), max(weights)
        weight_range = self.max_w - self.min_w
        
        for edge in self.edges:
            normalized, linewidth, alpha = self.get_linewidth_alpha(edge["weight"])
            edge["weight_normalized"] = normalized
            edge["linewidth"] = linewidth
            edge["alpha"] = alpha

    def get_linewidth_alpha(self, weight):
        """Get the line width and alpha values based on the edge weight."""
        normalized = (abs(weight) - self.min_w) / (self.max_w - self.min_w) if (self.max_w - self.min_w) else 1.0
        linewidth = MIN_THICKNESS + normalized * (MAX_THICKNESS - MIN_THICKNESS)
        alpha = MIN_ALPHA + normalized * (MAX_ALPHA - MIN_ALPHA)
        return normalized,linewidth, alpha

    def compute_graph_features(self):
        # Local features
        self.undirected_strengths = bct.strengths_und(self.undirected_connection_matrix)
        self.undirected_betweenness_centralities = bct.betweenness_wei(self.undirected_connection_matrix)
        self.undirected_clustering_coefs = bct.clustering_coef_wd(self.undirected_connection_matrix)
        self.local_efficiency = bct.efficiency_wei(self.undirected_connection_matrix, local=True)

        # Global features
        self.density = bct.density_und(self.undirected_connection_matrix)[0]
        self.global_efficiency = bct.efficiency_wei(self.undirected_connection_matrix)
        self.char_path_length = bct.charpath(self.undirected_connection_matrix)[0]
        self.undirected_transitivity_wu = bct.transitivity_wu(self.undirected_connection_matrix)
        
        # Derived metrics
        self.average_local_efficiency = np.average(self.local_efficiency)
        self.average_betweenness_centrality = np.average(self.undirected_betweenness_centralities)
