# Uses python3

"""
Problem: You have n candies. You would like to use these candies for top k places in a competition with a
natural restriction that a higher place gets a larger number of candies. To make as many children happy
as possible, you are going to find the largest value of k for which it is possible.

Mathematical formulation: Represent a given positive integer n as a sum of as many pairwise distinct
positive integers as possible.
"""

import sys


def optimal_summands(n):
    summands = []
    s = 1
    taken = 0
    while n - taken > 2*s:
        summands.append(s)
        taken += s
        s += 1
    if n - taken > 0:
        summands.append(n - taken)
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
