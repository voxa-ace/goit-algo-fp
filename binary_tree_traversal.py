import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    """
    Represents a node in a binary tree.

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

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Adds nodes and edges to a graph based on the binary tree structure.

    Args:
        graph (nx.DiGraph): The graph to which nodes and edges will be added.
        node (Node): The current node in the binary tree.
        pos (dict): Dictionary to hold position of nodes for visualization.
        x (float): The x-coordinate for the current node's position.
        y (float): The y-coordinate for the current node's position.
        layer (int): The current layer of the binary tree.
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def draw_tree(tree_root):
    """
    Visualizes the binary tree.

    Args:
        tree_root (Node): The root node of the binary tree.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_color_sequence(num_steps, start_color=(0, 0, 0), end_color=(255, 255, 255)):
    """
    Generates a color sequence from start color to end color.

    Args:
        num_steps (int): Number of steps in the sequence.
        start_color (tuple): RGB code of the start color.
        end_color (tuple): RGB code of the end color.

    Returns:
        List[tuple]: List of RGB color tuples.
    """
    color_step = [(end_color[i] - start_color[i]) / num_steps for i in range(3)]
    return [tuple(int(start_color[i] + color_step[i] * step) for i in range(3)) for step in range(num_steps)]

def rgb_to_hex(rgb):
    """
    Converts an RGB color to its hexadecimal representation.

    Args:
        rgb (tuple): The RGB color tuple.

    Returns:
        str: The hexadecimal color string.
    """
    return "#{:02x}{:02x}{:02x}".format(*rgb)

def traverse_and_color(node, mode='dfs'):
    """
    Traverses the binary tree and colors the nodes.

    Args:
        node (Node): The root node of the binary tree.
        mode (str): The mode of traversal ('dfs' or 'bfs').

    Returns:
        List[Node]: List of nodes in the order they were visited.
    """
    color_sequence = generate_color_sequence(10, (0, 0, 0), (255, 255, 255))
    order = []

    def dfs(node):
        if node:
            node.color = rgb_to_hex(color_sequence[len(order) % len(color_sequence)])
            order.append(node)
            dfs(node.left)
            dfs(node.right)

    def bfs(node):
        queue = [node]
        while queue:
            current = queue.pop(0)
            if current:
                current.color = rgb_to_hex(color_sequence[len(order) % len(color_sequence)])
                order.append(current)
                queue.append(current.left)
                queue.append(current.right)

    if mode == 'dfs':
        dfs(node)
    elif mode == 'bfs':
        bfs(node)

    return order

if __name__ == "__main__":
    # Create the tree
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # User input for traversal mode with validation
    while True:
        mode = input("Enter traversal mode (dfs or bfs): ").strip().lower()
        if mode in ['dfs', 'bfs']:
            break
        print("Invalid mode. Please enter 'dfs' or 'bfs'.")

    # Traversing the tree and changing node colors
    traverse_and_color(root, mode=mode)

    # Visualizing the tree
    draw_tree(root)
