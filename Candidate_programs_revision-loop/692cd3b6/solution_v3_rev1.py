import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    fives = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    (r1, c1), (r2, c2) = sorted(fives)
    top, bot = r1, r2
    left, right = min(c1, c2), max(c1, c2)
    b1r0, b1r1 = r1-1, r1+1
    b1c0, b1c1 = c1-1, c1+1
    b2r0, b2r1 = r2-1, r2+1
    b2c0, b2c1 = c2-1, c2+1
    for r in range(top, bot+1):
        for c in range(left, right+1):
            if not (b1r0 <= r <= b1r1 and b1c0 <= c <= b1c1) and not (b2r0 <= r <= b2r1 and b2c0 <= c <= b2c1):
                if grid[r][c] == 4:
                    grid[r][c] = 0
    for r in range(r1+2, r2):
        for c in range(left, right):
            if grid[r][c] == 0:
                grid[r][c] = 4
    return grid