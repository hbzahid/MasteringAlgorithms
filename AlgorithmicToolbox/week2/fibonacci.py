# Uses python3
def calc_fib(n):
    first = 0
    second = 1
    for i in range(n):
        first, second = second, first + second
    return first

n = int(input())
print(calc_fib(n))
