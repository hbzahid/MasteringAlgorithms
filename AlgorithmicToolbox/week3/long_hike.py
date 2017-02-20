"""
Problem description:

Input:
Weights w1, ... , wn and values v1, ... , vn of items; capacity W

Output:
The maximum total value of fractions of items that fit into a bag
of capacity W

Lemma:
There exists an optimal solution that uses as much as possible
of an item with the maximal value per unit of weight

Example:
    values: [20, 18, 14]
    weights: [4, 3, 2]
    all: [(4, 20), (3, 18), (2, 14)]
"""


def fractional_knapsack(weightedValues, capacity):
    totalValue = 0
    weightedValues.sort(key=lambda x: x[1] / x[0], reverse=True)
    amounts = [0] * len(weightedValues)
    for i, (weight, value) in enumerate(weightedValues):
        if capacity <= 0: break
        amount = min(capacity, weight)
        amounts[i] = amount
        totalValue += amount * (value / weight)
        capacity -= amount
    return {weightedValues[i]: amounts[i] for i in range(len(weightedValues))}

print(fractional_knapsack([(4, 20), (3, 18), (2, 14)], 7))