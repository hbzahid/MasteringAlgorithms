# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    weighted_values = [(weights[i], values[i]) for i in range(len(weights))]
    weighted_values.sort(key=lambda x: x[1] / x[0], reverse=True)
    for i, (w, v) in enumerate(weighted_values):
        if capacity <= 0: break
        amount = min(capacity, w)
        capacity -= amount
        value += amount * (v / w)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
