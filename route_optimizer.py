import networkx as nx

def get_optimized_route(predicted_traffic):
    """
    Calculates the best route using Dijkstra's Algorithm by adjusting 
    edge weights based on predicted traffic[cite: 177, 180, 233].
    """
    G = nx.Graph()
    
    # Map traffic levels to weight multipliers [cite: 178, 179]
    # Low = 1, Medium = 2, High = 3
    multiplier = {"Low": 1, "Medium": 2, "High": 3}.get(predicted_traffic, 1)
    
    # Define road segments (Nodes: Intersections, Edges: Roads) [cite: 229, 230]
    # format: (NodeA, NodeB, Base Weight * Multiplier)
    G.add_edge("City Center", "Main Street", weight=5 * multiplier)
    G.add_edge("Main Street", "Ring Road", weight=10 * multiplier)
    G.add_edge("Ring Road", "Highway Exit", weight=5)
    G.add_edge("City Center", "Highway Exit", weight=50) # Alternative long path

    # Find the path with the lowest total cost [cite: 176, 232]
    path = nx.dijkstra_path(G, "City Center", "Highway Exit", weight='weight')
    return path