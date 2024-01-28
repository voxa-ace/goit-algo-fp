import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.edges = {}

    def add_node(self, value):
        if value not in self.edges:
            self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

    def dijkstra(self, initial):
        visited = {node: False for node in self.edges}
        distances = {node: float('infinity') for node in self.edges}
        distances[initial] = 0
        queue = [(0, initial)]

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if visited[current_node]:
                continue

            visited[current_node] = True

            for neighbor, weight in self.edges[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances

def visualize_graph(graph):
    G = nx.Graph()
    for node, edges in graph.edges.items():
        for neighbor, weight in edges:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)  # Layout for node positioning

    # Draw nodes and edges
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1)

    # Draw edge labels
    edge_labels = {(node, neighbor): weight for node, edges in graph.edges.items() for neighbor, weight in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.axis('off')
    plt.show()

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 3)
    graph.add_edge("B", "C", 1)
    graph.add_edge("B", "D", 4)
    graph.add_edge("C", "D", 1)

    visualize_graph(graph)

    start_node = "A"
    distances = graph.dijkstra(start_node)
    print("Shortest distances from node", start_node)
    for node, distance in distances.items():
        print(node, ":", distance)
