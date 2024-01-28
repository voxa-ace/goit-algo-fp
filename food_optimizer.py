def greedy_algorithm(items, budget):
    """
    Selects food items to maximize calorie intake within a given budget using a greedy algorithm.
    
    Args:
        items (dict): A dictionary of food items with their cost and calorie values.
        budget (int): The available budget.

    Returns:
        tuple: A tuple containing a list of selected items and the total calorie value.
    """
    # Sort items by calorie-to-cost ratio
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    selected_items = []

    # Select items while staying within budget
    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            total_calories += info['calories']
            selected_items.append(item)
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    """
    Calculates the optimal set of food items to maximize calorie intake within a budget using dynamic programming.
    
    Args:
        items (dict): A dictionary of food items with their cost and calorie values.
        budget (int): The available budget.

    Returns:
        tuple: A tuple containing a list of selected items and the total calorie value.
    """
    # Check for valid input
    if not items or budget <= 0:
        return [], 0

    item_names = list(items.keys())
    item_costs = [items[name]['cost'] for name in item_names]
    item_calories = [items[name]['calories'] for name in item_names]

    # Initialize dynamic programming table
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    # Build the table
    for i in range(1, len(items) + 1):
        for w in range(1, budget + 1):
            if item_costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_costs[i - 1]] + item_calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Determine the selected items
    w = budget
    selected_items = []
    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= item_costs[i - 1]

    total_calories = dp[len(items)][budget]
    return selected_items[::-1], total_calories

# Test data
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

# Testing the greedy algorithm
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected Items:", selected_items_greedy)
print("Total Calories:", total_calories_greedy)

# Testing the dynamic programming algorithm
selected_items_dynamic, total_calories_dynamic = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Selected Items:", selected_items_dynamic)
print("Total Calories:", total_calories_dynamic)
