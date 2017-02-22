#Uses python3

"""
Problem: Compose the largest number out of a set of integers.

Example:
    Input: 91, 92
    Output: 9291

    Input: 91, 914
    Output: 91914
"""

import sys, functools


def cmp_fn(x, y):
    if int(x + y) >= int(y + x):
        return 1
    else:
        return -1


def largest_number(arr):
    salaries = [a.lstrip('0') for a in arr]
    salaries.sort(key=functools.cmp_to_key(cmp_fn), reverse=True)
    max_salary = ''.join(salaries)
    return max_salary


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
