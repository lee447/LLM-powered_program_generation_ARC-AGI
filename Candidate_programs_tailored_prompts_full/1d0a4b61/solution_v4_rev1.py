import numpy as np
def solve(grid):
    h, w = len(grid), len(grid[0])
    border_rows = []
    for i, row in enumerate(grid):
        s = {x for x in row if x != 0}
        if len(s) == 1:
            border_rows.append(i)
    border_rows.sort()
    p = border_rows[1] - border_rows[0]
    template = [None] * p
    for dr in range(p):
        for i in range(dr, h, p):
            if all(x != 0 for x in grid[i]):
                template[dr] = grid[i]
                break
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if out[r][c] == 0:
                out[r][c] = template[r % p][c]
    return out