#Uses python3

"""
Given an undirected graph and two distinct vertices x and y,
check if there is a path between x and y
"""

import sys

def reach(adj, x, y):
    visited[x] = True
    if x == y:
        return True
    for nbr in adj[x]:
        if not visited[nbr]:
            if reach(adj, nbr, y):
                return True
    return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    visited = [False] * n
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(int(reach(adj, x, y)))
