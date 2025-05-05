import numpy as np

def solve(grid):
    w = len(grid[0])
    apex = grid[0].index(2)
    out = [[0]*w for _ in range(w)]
    for r in range(w):
        l = apex - r
        rr = apex + r
        if 0 <= l < w:
            out[r][l] = 2
        if 0 <= rr < w:
            out[r][rr] = 2
    for r in range(w):
        lbound = max(0, apex - r)
        rbound = min(w-1, apex + r)
        m = r % 4
        for c in range(lbound, rbound+1):
            if out[r][c] == 0 and (c - apex) % 4 == m:
                out[r][c] = 1
    return out