# Uses python3
import sys


def fibonacci_rem(n, mod):
    current = 0
    next = 1
    for _ in range(n):
        current, next = next, (current + next) % mod
    return current


def fibonacci_sum_last_digit(n):
    period = 60 # pisano period for 10
    # Use the relation S(n) = F(n+2) - 1
    n = (n + 2) % period
    sum_last_digit = (fibonacci_rem(n, 10) - 1) % 10
    return sum_last_digit


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_last_digit(n))