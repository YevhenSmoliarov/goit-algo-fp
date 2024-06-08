#Завдання 5. Візуалізація обходу бінарного дерева
import queue

def bfs_visualization(root):
    if not root:
        return

    q = queue.Queue()
    q.put(root)
    step = 0

    while not q.empty():
        node = q.get()
        node.color = "#{:02x}{:02x}{:02x}".format(255 - step * 10, 0, step * 10)
        step += 1

        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

    draw_tree(root)

# Використання функції
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

bfs_visualization(root)