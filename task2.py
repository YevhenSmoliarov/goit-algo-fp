#Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії
import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, length, depth, ax):
    if depth == 0:
        return

    x2 = x + length * np.cos(np.radians(angle))
    y2 = y + length * np.sin(np.radians(angle))

    ax.plot([x, x2], [y, y2], color='green')

    draw_tree(x2, y2, angle - 20, length * 0.8, depth - 1, ax)
    draw_tree(x2, y2, angle + 20, length * 0.8, depth - 1, ax)

def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    draw_tree(0, 0, 90, 100, 10, ax)

    plt.show()

main()