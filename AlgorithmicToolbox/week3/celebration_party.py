"""
Problem description:
Organize children into the minimum possible number of groups
such that the age of any two children in the same group
differ by at most one year.

Mathematical formulation:
Input: A set of n points x0, ... , x(n-1)
Output: The minimum of segments of unit length needed to
cover all the points.

Safe move: cover the leftmost point with a unit segment with
left end in this point (easy to prove).

Example:

[2.1, 2.5, 2.8, 3.1, 3.4, 3.6, 3.8, 4.0, 5.5, 6.7]
"""

def min_groups(ages):
    n = len(ages)
    groups = []
    ages.sort()
    index = 0
    while index < n:
        left, right = ages[index], ages[index] + 1
        groups.append((left, right))
        index += 1
        while index < n and ages[index] <= right:
            index += 1
    return groups

assert(min_groups([2.1, 2.5, 2.8, 3.1, 3.4, 3.6, 3.8, 4.0, 5.5, 6.7]) == [(2.1, 3.1), (3.4, 4.4), (5.5, 6.5), (6.7, 7.7)])