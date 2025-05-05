def solve(grid):
    h, w = len(grid), len(grid[0])
    for row in grid:
        if any(c > 1 for c in row) and all(c != 0 for c in row):
            pattern = row
            break
    for p in range(1, w+1):
        if all(pattern[i] == pattern[i % p] for i in range(w)):
            cycle = pattern[:p]
            break
    out = []
    for row in grid:
        if any(c > 1 for c in row):
            out.append([cycle[i % len(cycle)] for i in range(w)])
        else:
            out.append([1] * w)
    return out