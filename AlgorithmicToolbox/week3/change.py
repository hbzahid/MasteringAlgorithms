# Uses python3
import sys

def get_change(m):
    denominations = [10, 5, 1]
    numCoins = 0
    for i, d in enumerate(denominations):
        numCoins += m // d
        m %= d
    return numCoins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
