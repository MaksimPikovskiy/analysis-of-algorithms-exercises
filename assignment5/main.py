# These are the functions and helper functions for the project questions from the Assignment #5
# Functions: fibDyn -> finds the nth Fibonacci number using dynamic programming
#            knapsack -> finds the maximum value that can be placed in the knapsack using dynamic programming
#            knapsackContents -> finds the sequence of items that maximize knapsack's value
# Helpers:   knapsackTable -> imitates knapsack function, getting the table of knapsack's value instead of
#                             maximum value of knapsack, to assist in retrieving the contents of knapsack
# Author: Maksim Pikovskiy, mp8671
# CSCI 261
# 11/12/2021


# Helper for Question #4c function
# Imitates knapsack function, but instead returns the table to get the contents of the knapsack
#
# This could be simplified by making the knapsack return the table and then get the best value, but that
# would go against what the problem is asking
#
# The given sequence (v, w) : ps is represented as two arrays, values and weights
# This was done for easier implementation and better visibility/readability
def knapsackTable(values, weights, weightLimit):
    if len(values) <= 0 or len(weights) <= 0:
        return 0
    elif weightLimit <= 0:
        return 0
    else:
        results = [[0 for x in range(weightLimit + 1)] for x in range(len(values) + 1)]

        for i in range(1, len(values) + 1):
            for j in range(1, weightLimit + 1):
                if weights[i - 1] > j:
                    results[i][j] = results[i - 1][j]
                else:
                    results[i][j] = max(values[i - 1] + results[i - 1][j - weights[i - 1]], results[i - 1][j])
    return results


# Question #3
# Dynamically finds the nth Fibonacci number (using dynamic programming)
def fibDyn(n):
    # base cases
    f = [0, 1]

    # dynamic approach to recursive calls
    for k in range(2, n + 1):
        f.append(f[k - 1] + f[k - 2])

    return f[n]


# Question #4b
# Dynamically finds the maximum value that can be placed in the knapsack
#
# The given sequence (v, w) : ps is represented as two arrays, values and weights
# This was done for easier implementation and better visibility/readability
def knapsack(values, weights, weightLimit):
    if len(values) <= 0 or len(weights) <= 0:
        return 0
    elif weightLimit <= 0:
        return 0
    else:
        results = [[0 for x in range(weightLimit + 1)] for x in range(len(values) + 1)]

        for i in range(1, len(values) + 1):
            for j in range(1, weightLimit + 1):
                if weights[i - 1] > j:
                    results[i][j] = results[i - 1][j]
                else:
                    results[i][j] = max(values[i - 1] + results[i - 1][j - weights[i - 1]], results[i - 1][j])

        return results[len(values)][weightLimit]


# Question 4c
# Finds the sequence of items that maximizes knapsack's value
#
# The given sequence (v, w) : ps is represented as two arrays, values and weights
# This was done for easier implementation and better visibility/readability
def knapsackContents(values, weights, weightLimit):
    # Retrieve the table for the values of knapsack with different combinations
    results = knapsackTable(values, weights, weightLimit)

    # Retrieve the best value of knapsack
    bestValue = results[len(values)][weightLimit]

    valuesKnapsack = []
    weightsKnapsack = []

    # Go through the table to get the contents
    weight = weightLimit
    for i in range(len(values), 0, -1):
        if bestValue <= 0:
            break
        elif bestValue == results[i - 1][weight]:
            continue
        else:
            valuesKnapsack.append(values[i - 1])
            weightsKnapsack.append(weights[i - 1])

            bestValue = bestValue - values[i - 1]
            weight = weight - weights[i - 1]

    return valuesKnapsack, weightsKnapsack


# Main function that tests the function for the project question
def main() -> None:
    print("fibDyn()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Let n = 5: fibDyn(5) -> ", fibDyn(5))
    print("Let n = 10: fibDyn(10) -> ", fibDyn(10))
    print("Let n = 25: fibDyn(25) -> ", fibDyn(25))
    print("Let n = 50: fibDyn(50) -> ", fibDyn(50))
    print("Let n = 100: fibDyn(100) -> ", fibDyn(100))

    print("\n\nknapsack()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    vs = [60, 100, 120]
    ws = [10, 20, 30]
    W = 50
    print("Let values = [60, 100, 120], weights = [10, 20, 30], and weightLimit = 50: "
          "knapsack(values, weights, weightLimit) -> ", knapsack(vs, ws, W))
    vs = [20, 5, 10, 40, 15, 25]
    ws = [1, 2, 3, 8, 7, 4]
    W = 10
    print("Let values = [20, 5, 10, 40, 15, 25], weights = [1, 2, 3, 8, 7, 4], and weightLimit = 10: "
          "knapsack(values, weights, weightLimit) -> ", knapsack(vs, ws, W))
    vs = [10, 40, 50, 70]
    ws = [1, 3, 4, 5]
    W = 8
    print("Let values = [10, 40, 50, 70], weights = [1, 3, 4, 5], and weightLimit = 8: "
          "knapsack(values, weights, weightLimit) -> ", knapsack(vs, ws, W))

    print("\n\nknapsackContents()-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    vs = [60, 100, 120]
    ws = [10, 20, 30]
    W = 50
    print("Let values = [60, 100, 120], weights = [10, 20, 30], and weightLimit = 50: "
          "knapsackContents(values, weights, weightLimit) -> ")
    bestValues, bestWeights = knapsackContents(vs, ws, W)
    bestValues.sort()
    bestWeights.sort()
    print("Values: ", bestValues, "\nWeights: ", bestWeights)

    vs = [20, 5, 10, 40, 15, 25]
    ws = [1, 2, 3, 8, 7, 4]
    W = 10
    print("\nLet values = [20, 5, 10, 40, 15, 25], weights = [1, 2, 3, 8, 7, 4], and weightLimit = 10: "
          "knapsackContents(values, weights, weightLimit) -> ")
    bestValues, bestWeights = knapsackContents(vs, ws, W)
    bestValues.sort()
    bestWeights.sort()
    print("Values: ", bestValues, "\nWeights: ", bestWeights)

    vs = [10, 40, 50, 70]
    ws = [1, 3, 4, 5]
    W = 8
    print("\nLet values = [10, 40, 50, 70], weights = [1, 3, 4, 5], and weightLimit = 8: "
          "knapsackContents(values, weights, weightLimit) -> ")
    bestValues, bestWeights = knapsackContents(vs, ws, W)
    bestValues.sort()
    bestWeights.sort()
    print("Values: ", bestValues, "\nWeights: ", bestWeights)


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()
