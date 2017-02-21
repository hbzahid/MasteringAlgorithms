# Uses python3

"""
Given a set of n segments {[a0, b0], [a1, b1], . . . , [a(n-1), b(n-1)]} with integer coordinates
on a line, find the minimum number m of points such that each segment contains at least one point.
"""

import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    segments.sort(key=lambda s: s.end)
    i = 0
    while i < len(segments):
        right = segments[i].end
        points.append(right)
        i += 1
        while i < len(segments) and segments[i].start <= right:
            i += 1
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')