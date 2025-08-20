from PyQt5.QtWidgets import QApplication
import sys
import time
import threading
from Arrow import Arrow
import WeightedVisibilityGraph
import MRSightUI


class MRSight(MRSightUI.MRSightMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_event_connections()
        self.initialize_data()
        self.initialize_visualization()

    def setup_event_connections(self):
        """Set up event handlers for the matplotlib canvas."""
        self.graph_widget.figure.canvas.mpl_connect("motion_notify_event", self.on_hover)
        self.graph_widget.figure.canvas.mpl_connect("button_press_event", self.on_click)

    def initialize_data(self):
        """Initialize subject data and graphs."""
        self.subject_index = self.primary_subject_combo.currentIndex()
        self.comparison_subject_index = self.comparison_subject_combo.currentIndex()
        self.primary_graph = WeightedVisibilityGraph.Graph(self.subject_index)
        self.comparison_graph = WeightedVisibilityGraph.Graph(self.comparison_subject_index)
        self.selected_metabolite = None
        self._double_click_detected = False
        self.edge_artists = []
        self.all_y = []

    def initialize_visualization(self):
        """Initialize the visualization components."""
        self.draw_spectrum()
        self.draw_graph()
        self.write_global_features()

    def draw_spectrum(self):
        """Draw the spectrum visualization."""
        self.spectrum_widget.axes.clear()
        self.spectrum_widget.axes.grid(True)
        
        # Plot primary spectrum
        self.spectrum_widget.axes.plot(
            WeightedVisibilityGraph.chemical_shifts_array,
            self.primary_graph.current_spectrum, 
            linewidth=0.5
        )
        
        # Plot comparison spectrum if enabled
        if self.enable_comparison_check.isChecked():
            self.spectrum_widget.axes.plot(
                WeightedVisibilityGraph.chemical_shifts_array,
                self.comparison_graph.current_spectrum,
                linewidth=0.2, 
                color='red'
            )
            
        self.spectrum_widget.axes.set_xlabel("Chemical Shift (ppm)")
        self.spectrum_widget.axes.set_ylabel("Signal Intensity")

        # Draw vertical lines for metabolites
        for node in self.primary_graph.nodes:
            if self.checkboxes[node["name"]].isChecked():
                self.spectrum_widget.axes.axvline(
                    x=node["coordinates"][0], 
                    color=MRSightUI.colors[node["name"]], 
                    linestyle='--', 
                    label=node["name"], 
                    linewidth=0.5
                )

        self.spectrum_widget.axes.invert_xaxis()
        self.spectrum_widget.figure.canvas.draw_idle()

    def draw_graph(self):
        """Draw the graph visualization."""
        self.graph_widget.axes.clear()
        self.graph_widget.axes.grid(True)
        self.edge_artists = []
        self.all_y = []
        
        # Setup tooltips
        self.setup_tooltips()
        
        # Draw edges
        self.draw_edges()
        
        # Toggle comparison mode if enabled
        self.toggle_comparison_mode(self.enable_comparison_check.isChecked())
        
        # Draw nodes
        self.draw_nodes()
        
        # Set graph limits and labels
        self.configure_graph_display()

    def setup_tooltips(self):
        """Initialize tooltips for the graph."""
        self.edges_tooltip = self.graph_widget.axes.annotate(
            "", xy=(0, 0), xytext=(15, 15), textcoords="offset points",
            bbox=dict(boxstyle="round", fc="red", alpha=0.8),
            ha="center"
        )
        self.nodes_tooltip = self.graph_widget.axes.annotate(
            "", xy=(0, 0), xytext=(15, 15), textcoords="offset points",
            bbox=dict(boxstyle="round", fc="blue", alpha=0.8),
            ha="center"
        )
        self.nodes_tooltip.set_visible(False)
        self.edges_tooltip.set_visible(False)

    def draw_edges(self):
        """Draw graph edges."""
        for edge in self.primary_graph.edges:
            from_name = edge["source"]
            to_name = edge["target"]

            # Check if edge should be displayed
            if not self.should_display_edge(from_name, to_name):
                continue

            x1, y1 = [node["coordinates"] for node in self.primary_graph.nodes if node["name"] == from_name][0]
            x2, y2 = [node["coordinates"] for node in self.primary_graph.nodes if node["name"] == to_name][0]
            
            arrow = self.create_arrow(x1, y1, x2, y2, from_name, to_name, edge["linewidth"], edge["alpha"], 
                                      edge["weight"])
            
            if arrow:
                self.graph_widget.axes.add_patch(arrow)
                self.edge_artists.append(arrow)
                
            self.all_y.extend([y1, y2])

    def should_display_edge(self, from_name, to_name):
        """Check if an edge should be displayed based on current selection."""
        both_checked = (self.checkboxes[from_name].isChecked() and self.checkboxes[to_name].isChecked())
        selected_involved = (self.selected_metabolite == from_name or self.selected_metabolite == to_name)
        
        return both_checked or selected_involved

    def create_arrow(self, x1, y1, x2, y2, from_name, to_name, linewidth, alpha, weight):
        """Create an arrow for the graph."""
        arrow = Arrow(
            posA=(x1, y1), 
            posB=(x2, y2),
            arrowstyle="->",
            linewidth=linewidth,
            alpha=alpha,
            color=MRSightUI.colors[from_name],
            mutation_scale=15
        )

        arrow.meta = {
            "source": from_name,
            "target": to_name,
            "ratio": weight
        }
        
        if self.selected_metabolite is not None:
            selected_involved = (self.selected_metabolite == from_name or self.selected_metabolite == to_name)
            both_checked = (self.checkboxes[from_name].isChecked() and self.checkboxes[to_name].isChecked())
            
            if not (selected_involved and both_checked):
                return None
            
            arrow.set_color(MRSightUI.colors[self.selected_metabolite])
            
        return arrow

    def draw_nodes(self):
        """Draw graph nodes."""
        for node in self.primary_graph.nodes:
            if not self.checkboxes[node["name"]].isChecked():
                continue
                
            x, y = node["coordinates"]
            color = MRSightUI.colors[node["name"]]
            alpha = 1.0
            size = 8
            
            if self.selected_metabolite is not None:
                if self.selected_metabolite != node["name"]:
                    alpha = 0.2
            
            # Draw node
            self.graph_widget.axes.plot(x, y, marker="o", color=color, markersize=size, alpha=alpha)
            
            # Draw vertical line
            self.graph_widget.axes.axvline(
                x=x, color=color, linestyle='--', label=node["name"], linewidth=1
            )

    def configure_graph_display(self):
        """Configure graph display properties."""
        # Set axis limits if we have data
        if self.all_y and self.primary_graph.nodes:
            all_x = [node["coordinates"][0] for node in self.primary_graph.nodes]
            min_y, max_y = min(self.all_y), max(self.all_y)
            bottom_y_limit = min_y * 1.5 if min_y < 0 else min_y - (0.5 * min_y)
            
            self.graph_widget.axes.set_xlim(min(all_x) - 2, max(all_x) + 2)
            self.graph_widget.axes.set_ylim(bottom_y_limit, max_y * 1.05)

        # Set labels and finalize
        self.graph_widget.axes.set_xlabel("Chemical Shift (ppm)")
        self.graph_widget.axes.set_ylabel("Metabolite Intensity")
        self.graph_widget.axes.invert_xaxis()
        self.graph_widget.axes.legend(loc='upper right')
        self.graph_widget.axes.figure.canvas.draw_idle()

    def toggle_comparison_mode(self, state):
        """Toggle display of comparison subject data."""
        self.draw_spectrum()
        
        if state and self.selected_metabolite is not None:
            self.draw_comparison_data()
            
        self.write_global_features()

    def draw_comparison_data(self):
        """Draw comparison data when enabled."""
        # Draw comparison edges
        for edge in self.comparison_graph.edges:
            source_name = edge["source"]
            target_name = edge["target"]
            
            if ((edge["source"] == self.selected_metabolite or edge["target"] == self.selected_metabolite) and 
                self.checkboxes[source_name].isChecked() and self.checkboxes[target_name].isChecked()):
                
                x1, y1 = [node["coordinates"] for node in self.comparison_graph.nodes if node["name"] == source_name][0]
                x2, y2 = [node["coordinates"] for node in self.comparison_graph.nodes if node["name"] == target_name][0]
                
                arrow = Arrow(
                    posA=(x1, y1), posB=(x2, y2),
                    arrowstyle="->",
                    linewidth=edge["linewidth"],
                    alpha=edge["alpha"],
                    color='white',
                    mutation_scale=15
                )
                
                arrow.meta = {
                    "source": source_name,
                    "target": target_name,
                    "ratio": edge["weight"]
                }

                self.graph_widget.axes.add_patch(arrow)
                self.edge_artists.append(arrow)
                self.all_y.extend([y1, y2])
        
        # Draw comparison nodes
        for node in self.comparison_graph.nodes:
            if self.checkboxes[node["name"]].isChecked():
                self.graph_widget.axes.plot(
                    node["coordinates"][0], 
                    node["coordinates"][1], 
                    marker="o",
                    color='white', 
                    markersize=8, 
                    alpha=0.2
                )

    def on_hover(self, event):
        """Handle hover events over the graph."""
        if event.inaxes != self.graph_widget.axes:
            return

        # Check for hovering over edges
        self.handle_edge_hover(event)
        
        # Check for hovering over nodes
        self.handle_node_hover(event)
        
        self.graph_widget.figure.canvas.draw_idle()

    def handle_edge_hover(self, event):
        """Handle hover over graph edges."""
        visible = False
        for arrow in self.edge_artists:
            contains, _ = arrow.contains(event)
            if contains:
                meta = arrow.meta
                self.edges_tooltip.xy = (event.xdata, event.ydata)
                self.edges_tooltip.set_text(
                    f"{meta['source']} → {meta['target']}\n"
                    f"Ratio: {meta['ratio']:.4f}"
                )
                self.edges_tooltip.set_visible(True)
                visible = True
                break

        if not visible:
            self.edges_tooltip.set_visible(False)

    def handle_node_hover(self, event):
        """Handle hover over graph nodes."""
        visible = False
        if not self.enable_node_metadata_check.isChecked():
            return
            
        for index, node in enumerate(self.primary_graph.nodes):
            if not (self.checkboxes[node["name"]].isChecked() or self.selected_metabolite == node["name"]):
                continue
                
            # Calculate distance from cursor to node
            distance = abs(event.xdata - node["coordinates"][0])

            # If cursor is close enough to the node
            if distance < 0.3:  # Threshold for detection
                self.nodes_tooltip.xy = (event.xdata, event.ydata)
                self.nodes_tooltip.set_backgroundcolor(MRSightUI.colors[node["name"]])
                
                # Format node metadata
                node_metadata = self.format_node_metadata(node, index)
                
                self.nodes_tooltip.set_text(node_metadata)
                self.nodes_tooltip.set_visible(True)
                visible = True
                break
                
        if not visible:
            self.nodes_tooltip.set_visible(False)

    def format_node_metadata(self, node, index):
        """Format node metadata for tooltip display."""
        metadata = [f"{node['name']}"]
        metadata.append(f"Intensity: {node['coordinates'][1]:.2f}")
        
        if node['name'] != "PCr":
            metadata.append(f"Ratio to PCr: {node['pcr_ratio']:.4f}")
            
        metadata.append(f"Strength: {self.primary_graph.undirected_strengths[index]:.2f}")
        metadata.append(f"Betweenness Centrality: {self.primary_graph.undirected_betweenness_centralities[index]:.2f}")
        metadata.append(f"Clustering Coefficient: {self.primary_graph.undirected_clustering_coefs[index]:.2f}")
        metadata.append(f"Node Efficiency: {self.primary_graph.local_efficiency[index]:.2f}")
        metadata.append(f"Assortativity Coefficient Pos: {self.primary_graph.assortativity_coefs_pos[index]:.2f}")
        
        return "\n".join(metadata)

    def on_click(self, event):
        """Handle click events on the graph."""
        if event.inaxes != self.graph_widget.axes:
            return

        # Check for clicks on edges
        for arrow in self.edge_artists:
            contains, _ = arrow.contains(event)
            if contains:
                self.handle_edge_click(arrow, event)
                return

        # Check for double-clicks to select metabolites
        if event.dblclick:
            self.handle_node_selection(event)

    def handle_edge_click(self, arrow, event):
        """Handle clicks on graph edges."""
        if event.dblclick:
            # Toggle transparency
            current_alpha = arrow.get_alpha() or 1.0
            new_alpha = 0.2 if current_alpha > 0.5 else 1.0
            arrow.set_alpha(new_alpha)
            self.graph_widget.figure.canvas.draw_idle()
            self._double_click_detected = True
        else:
            # Delay single click to handle potential double clicks
            def delayed_single_click():
                time.sleep(0.25)  # wait to see if double click happens
                if not getattr(self, "_double_click_detected", False):
                    self.flip_edge(arrow)
                    self.graph_widget.figure.canvas.draw_idle()
                else:
                    self._double_click_detected = False

            threading.Thread(target=delayed_single_click).start()

    def handle_node_selection(self, event):
        """Handle double-click node selection."""
        min_distance = float('inf')
        closest_metabolite = None

        for node in self.primary_graph.nodes:
            distance = abs(event.xdata - node["coordinates"][0])
            if distance < min_distance:
                min_distance = distance
                closest_metabolite = node["name"]

        if min_distance < 0.2:
            if self.selected_metabolite == closest_metabolite:
                self.selected_metabolite = None
            else:
                self.selected_metabolite = closest_metabolite

            self.draw_graph()

    def write_global_features(self):
        """Update the display of global graph features."""
        self.primary_global_features_text.setHtml(MRSightUI.style_global_features(
            self.subject_index, self.primary_graph
        ))
        
        state = self.enable_comparison_check.isChecked()
        if state:
            self.comparison_global_features_text.setHtml(MRSightUI.style_global_features(
                self.comparison_subject_index, self.comparison_graph
            ))
            
        self.comparison_global_features_text.setVisible(state)

    def change_subject(self, index):
        """Change the primary subject being displayed."""
        self.subject_index = index
        self.primary_graph.change_subject(self.subject_index)
        self.draw_spectrum()
        self.draw_graph()
        self.write_global_features()
        self.graph_group.setTitle(f"Ratio-Weighted {self.primary_graph.graph_type} - Subject: {index+1}")
        self.spectrum_group.setTitle(f"MRS Spectrum - Subject: {self.subject_index+1}")

    def change_comparison_subject(self, index):
        """Change the comparison subject being displayed."""
        self.comparison_subject_index = index
        self.comparison_graph.change_subject(self.comparison_subject_index)
        self.draw_graph()
        self.write_global_features()
    
    def change_graph_type(self, type):
        """Change the type of graph being displayed."""
        self.primary_graph.change_graph_type(type)
        self.comparison_graph.change_graph_type(type)
        self.draw_graph()
        self.write_global_features()
        self.graph_group.setTitle(f"Ratio-Weighted {type} - Subject: {self.subject_index+1}")

    def flip_edge(self, edge_artist):
        """Flip the direction and ratio of an edge."""
        meta = edge_artist.meta
        meta["ratio"] = 1 / meta["ratio"] if meta["ratio"] != 0 else 0
        meta["source"], meta["target"] = meta["target"], meta["source"]
        edge_artist.set_positions(edge_artist.posB, edge_artist.posA)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MRSight()
    window.show()
    sys.exit(app.exec_())
