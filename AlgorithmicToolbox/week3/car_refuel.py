# array of distances [x0, x1, x2,..., x(n-1)] from A to B
# given the capacity of a car, minimize the number of refills
# Example: [375, 650, 750, 1000, 1400, 1750, 2000], capacity = 400 gives 4

def min_refills(A, capacity):
    numStops = len(A)
    numRefills = 0
    curRefill = 0
    while curRefill < numStops - 1:
        lastRefill = curRefill
        while (curRefill < numStops - 1) and (A[curRefill+1] - A[lastRefill] <= capacity):
            curRefill += 1
        if curRefill == lastRefill:
            return 'IMPOSSIBLE'
        if curRefill < numStops - 1:
            numRefills += 1
    return numRefills

assert(min_refills([375, 650, 750, 1000, 1400, 1750, 2000], 400) == 4)