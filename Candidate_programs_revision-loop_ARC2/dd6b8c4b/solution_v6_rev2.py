import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    core = [(i, j) for i in range(h) for j in range(w) if grid[i][j] in (2, 3)]
    if not core:
        return out
    rs, cs = zip(*core)
    r1, r2 = min(rs), max(rs)
    c1, c2 = min(cs), max(cs)
    H1, W1 = r2 - r1 + 1, c2 - c1 + 1
    n9 = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 9]
    if not n9:
        return out
    r9s, c9s = zip(*n9)
    r9min, r9max = min(r9s), max(r9s)
    c9min, c9max = min(c9s), max(c9s)
    H9, W9 = r9max - r9min + 1, c9max - c9min + 1
    rows = np.linspace(r9min, r9min + H9, H1 + 1, dtype=int)
    cols = np.linspace(c9min, c9min + W9, W1 + 1, dtype=int)
    for di in range(H1):
        for dj in range(W1):
            rs0, rs1 = rows[di], rows[di + 1]
            cs0, cs1 = cols[dj], cols[dj + 1]
            found = False
            for i in range(rs0, rs1):
                for j in range(cs0, cs1):
                    if 0 <= i < h and 0 <= j < w and grid[i][j] == 9:
                        found = True
                        break
                if found:
                    break
            if found:
                out[r1 + di][c1 + dj] = 9
    return out