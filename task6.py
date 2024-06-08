#Завдання 6. Жадібні алгоритми та динамічне програмування
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    selected_items = []
    total_calories = 0
    total_cost = 0

    for item, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected_items.append(item)
            total_calories += info["calories"]
            total_cost += info["cost"]

    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.keys())
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            cost = items[item_list[i-1]]["cost"]
            calories = items[item_list[i-1]]["calories"]
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(item_list[i-1])
            w -= items[item_list[i-1]]["cost"]

    return selected_items, dp[n][budget]

budget = 100
print("Greedy Algorithm Result:", greedy_algorithm(items, budget))
print("Dynamic Programming Result:", dynamic_programming(items, budget))