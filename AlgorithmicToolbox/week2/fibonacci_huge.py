# Uses python3

import sys

def next_fibonacci(mod):
    prev = 0
    current = 1
    while True:
        yield prev
        prev, current = current, (prev + current) % mod


def fibonacci_rem(n, mod):
    current = 0
    next = 1
    for _ in range(n):
        current, next = next, (current + next) % mod
    return current


def pisano_length(m):
    fib_array = []
    period_found = False
    fib_gen = next_fibonacci(m)
    while not period_found:
        fib_array.append(next(fib_gen))
        ptr_2 = len(fib_array) - 1
        ptr_1 = ptr_2 // 2
        while fib_array[ptr_1] == fib_array[ptr_2] and ptr_2 > 0:
            ptr_1 -= 1; ptr_2 -= 1
            period_found = ptr_1 < 0
    return len(fib_array) // 2


def get_fibonacci_huge(n, m):
    period = pisano_length(m)
    n = n % period
    return fibonacci_rem(n, m)


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))