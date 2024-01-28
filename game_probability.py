import random
import matplotlib.pyplot as plt

def roll_dice():
    """
    Simulates rolling two dice and returns the sum of their values.
    
    Returns:
        int: Sum of the two dice rolls.
    """
    return random.randint(1, 6) + random.randint(1, 6)

def simulate_dice_rolls(n):
    """
    Simulates rolling two dice n times and counts the frequency of each sum.

    Args:
        n (int): Number of simulations to run.

    Returns:
        dict: A dictionary with the sum as keys and their frequencies as values.
    """
    roll_counts = {total: 0 for total in range(2, 13)}

    for _ in range(n):
        roll = roll_dice()
        roll_counts[roll] += 1

    return roll_counts

def calculate_probabilities(roll_counts, n):
    """
    Calculates the probabilities of each sum based on the simulation.

    Args:
        roll_counts (dict): Dictionary with sums and their frequencies.
        n (int): Total number of simulations.

    Returns:
        dict: A dictionary with the sum as keys and their probabilities as values.
    """
    probabilities = {total: count / n for total, count in roll_counts.items()}
    return probabilities

# Number of simulations
n = 1000000

# Simulate dice rolls
roll_counts = simulate_dice_rolls(n)

# Calculate probabilities
probabilities = calculate_probabilities(roll_counts, n)

# Print the results
print("Sum\tProbability (Monte Carlo)")
for sum, prob in probabilities.items():
    print(f"{sum}\t{prob:.2%}")

# Plotting the results
sums = list(probabilities.keys())
probs = list(probabilities.values())

plt.figure(figsize=(10, 6))
plt.bar(sums, probs, color='skyblue')
plt.xlabel('Sum of Dice')
plt.ylabel('Probability')
plt.title('Probability Distribution of Dice Rolls (Monte Carlo Simulation)')
plt.xticks(range(2, 13))
plt.show()
