import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Node:
    """
    A class to represent a node in a binary tree.

    Attributes:
        left (Node): Left child of the node.
        right (Node): Right child of the node.
        val (Any): The value stored in the node.
        color (str): The color of the node for visualization.
        id (str): A unique identifier for the node.
    """
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_node(heap, key):
    """
    Add a new key to the heap and then build a binary tree based on the heap.

    Args:
        heap (List): The heap where the new key will be added.
        key (Any): The key to be added to the heap.

    Returns:
        Node: The root node of the binary tree.
    """
    heapq.heappush(heap, key)
    return build_tree(heap)

def build_tree(heap):
    """
    Build a binary tree based on the given heap.

    Args:
        heap (List): The heap used to build the tree.

    Returns:
        Node: The root node of the binary tree.
    """
    nodes = [Node(k) for k in heap]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    return nodes[0] if nodes else None

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Add nodes and edges to a graph from a binary tree.

    Args:
        graph (nx.DiGraph): The graph to which nodes and edges will be added.
        node (Node): The current node in the binary tree.
        pos (dict): Dictionary to hold position of nodes for visualization.
        x (float): The x-coordinate for the current node's position.
        y (float): The y-coordinate for the current node's position.
        layer (int): The current layer of the binary tree.

    Returns:
        nx.DiGraph: The updated graph with added nodes and edges.
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap):
    """
    Visualize a binary heap using matplotlib and networkx.

    Args:
        heap (List): The heap to be visualized.
    """
    tree_root = build_tree(heap)
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)} if tree_root else {}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Usage
heap = []
add_node(heap, 5)
add_node(heap, 3)
add_node(heap, 9)
add_node(heap, 1)
add_node(heap, 4)

# Generating a Binary Heap visualization
draw_heap(heap)
