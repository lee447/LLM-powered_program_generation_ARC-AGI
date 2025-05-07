import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    fives = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    (r1, c1), (r2, c2) = sorted(fives)
    top, bot = r1, r2
    left, right = min(c1, c2), max(c1, c2)
    for r in range(top, bot+1):
        for c in range(left, right+1):
            if grid[r][c] not in (2, 5):
                grid[r][c] = 4
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 4 and not (top <= r <= bot and left <= c <= right):
                grid[r][c] = 0
    return grid