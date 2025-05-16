import numpy as np
def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    stripes = {}
    for r in range(h):
        c = grid[r][2]
        if c not in (6, 7):
            stripes.setdefault(c, []).append(r)
    first = True
    for c, rs in stripes.items():
        if len(rs) == 2 and rs[1] - rs[0] == 2:
            r1, r2 = rs
            rm = r1 + 1
            row0 = grid[r1]
            pos = [i for i, v in enumerate(row0) if v == c]
            c_max = pos[-1]
            if first:
                first = False
                if c_max + 1 < w:
                    out[r1][c_max + 1] = 6
                out[rm][w - 1] = 6
            else:
                if c_max + 1 < w:
                    out[rm][c_max + 1] = 6
    for c, rs in stripes.items():
        if len(rs) == 1 and rs[0] == h - 1:
            r = rs[0]
            row = grid[r]
            pos = [i for i, v in enumerate(row) if v == c]
            c_max = pos[-1]
            if c_max + 1 < w:
                out[r][c_max + 1] = 6
    return out