import networkx as nx

def horizontal_visibility_graph(series):
    n = len(series)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            if all(series[k] < min(series[i], series[j]) for k in range(i + 1, j)):
                G.add_edge(i, j)
            else:
                break
    return G
