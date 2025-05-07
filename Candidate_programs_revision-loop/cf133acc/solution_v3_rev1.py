import numpy as np
def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    Hs = []
    for i, row in enumerate(grid):
        cnts = {}
        for v in row:
            if v:
                cnts[v] = cnts.get(v, 0) + 1
        if any(v >= 3 for v in cnts.values()):
            Hs.append(i)
    for H in sorted(Hs):
        row = grid[H]
        cols_by_color = {}
        for j, v in enumerate(row):
            if v:
                cols_by_color.setdefault(v, []).append(j)
        for c, js in cols_by_color.items():
            if len(js) < 3: continue
            c1, c2 = min(js), max(js)
            for j in range(c1, c2+1):
                out[H][j] = c
            pivot = None
            for j in range(c1, c2+1):
                if grid[H][j] == 0:
                    pivot = j
                    break
            if pivot is None:
                continue
            for i in range(H-1, -1, -1):
                if grid[i][pivot] == 0 and out[i][pivot] == 0:
                    out[i][pivot] = c
                else:
                    break
    return out