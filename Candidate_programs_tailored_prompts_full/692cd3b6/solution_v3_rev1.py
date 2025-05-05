import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 5]
    (r1, c1), (r2, c2) = pts
    up, down = ((r1, c1), (r2, c2)) if r1 < r2 else ((r2, c2), (r1, c1))
    left, right = ((r1, c1), (r2, c2)) if c1 < c2 else ((r2, c2), (r1, c1))
    if r1 < r2 and c1 < c2:
        rs, re = up[0] + 2, down[0] - 2
        cs, ce = left[1], right[1] - 2
    elif r1 > r2 and c1 > c2:
        rs, re = down[0] + 2, up[0] - 2
        cs, ce = right[1], left[1] - 2
    elif r1 < r2 and c1 > c2:
        rs, re = up[0] + 2, down[0] - 2
        cs, ce = down[1], up[1] + 2
    else:
        rs, re = down[0] + 2, up[0] - 2
        cs, ce = up[1], down[1] + 2
    rs, re = max(0, min(rs, re)), min(h - 1, max(rs, re))
    cs, ce = max(0, min(cs, ce)), min(w - 1, max(cs, ce))
    out = [row[:] for row in grid]
    for i in range(rs, re + 1):
        for j in range(cs, ce + 1):
            if out[i][j] == 0:
                out[i][j] = 4
    return out