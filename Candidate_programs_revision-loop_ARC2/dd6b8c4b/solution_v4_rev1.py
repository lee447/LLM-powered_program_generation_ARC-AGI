import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    pts = [(i, j) for i in range(h) for j in range(w) if grid[i][j] in (2, 3)]
    if not pts:
        return g
    rs = [i for i, _ in pts]
    cs = [j for _, j in pts]
    r1, r2 = min(rs), max(rs)
    c1, c2 = min(cs), max(cs)
    H1, W1 = r2 - r1 + 1, c2 - c1 + 1
    n9 = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 9]
    if not n9:
        return g
    rs9 = [i for i, _ in n9]
    cs9 = [j for _, j in n9]
    r9min, r9max = min(rs9), max(rs9)
    c9min, c9max = min(cs9), max(cs9)
    H9, W9 = r9max - r9min + 1, c9max - c9min + 1
    row_edges = [r9min + (k * H9) // H1 for k in range(H1 + 1)]
    col_edges = [c9min + (k * W9) // W1 for k in range(W1 + 1)]
    for di in range(H1):
        for dj in range(W1):
            rs0, rs1 = row_edges[di], row_edges[di+1]
            cs0, cs1 = col_edges[dj], col_edges[dj+1]
            found = False
            for i in range(rs0, rs1):
                for j in range(cs0, cs1):
                    if 0 <= i < h and 0 <= j < w and grid[i][j] == 9:
                        found = True
                        break
                if found:
                    break
            if found and g[r1+di][c1+dj] != 2:
                g[r1+di][c1+dj] = 9
    return g