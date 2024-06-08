#Завдання 7. Використання методу Монте-Карло
import random
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(trials):
    results = [0] * 11  # Для результатів від 2 до 12

    for _ in range(trials):
        roll = random.randint(1, 6) + random.randint(1, 6)
        results[roll - 2] += 1

    probabilities = [result / trials for result in results]
    return probabilities

trials = 10000
probabilities = monte_carlo_dice_simulation(trials)

# Аналітичні ймовірності
analytical_probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

# Побудова графіку
plt.plot(range(2, 13), probabilities, label="Monte Carlo")
plt.plot(range(2, 13), analytical_probabilities, label="Analytical")
plt.xlabel("Sum of dice")
plt.ylabel("Probability")
plt.legend()
plt.show()