#Завдання 4. Візуалізація піраміди
import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Additional argument to store node color
        self.id = str(uuid.uuid4())  # Unique identifier for each node

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

def build_tree(index, heap):
    if index >= len(heap):
        return None
    node = Node(heap[index])
    node.left = build_tree(2 * index + 1, heap)
    node.right = build_tree(2 * index + 2, heap)
    return node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Use id and store node value
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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Use node value for labels

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def create_heap_visualization(heap):
    def build_tree_recursive(index):
        if index >= len(heap):
            return None
        node = Node(heap[index])
        node.left = build_tree_recursive(2 * index + 1)
        node.right = build_tree_recursive(2 * index + 2)
        return node

    root = build_tree_recursive(0)
    draw_tree(root)

# Example usage
heap = BinaryHeap()
values = [15, 10, 8, 12, 20, 5, 4]
for value in values:
    heap.insert(value)

create_heap_visualization(heap.heap)