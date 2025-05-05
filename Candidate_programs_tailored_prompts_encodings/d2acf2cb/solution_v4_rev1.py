import numpy as np
def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    anchors = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 4]
    by_row = {}
    for r, c in anchors:
        by_row.setdefault(r, []).append(c)
    for r, cols in by_row.items():
        if len(cols) == 2 and 0 < r < h-1:
            cols.sort()
            c1, c2 = cols
            for c in range(c1+1, c2):
                res[r][c] = 8 if (c == c1+1 or c == c2-1) else 7
    by_col = {}
    for r, c in anchors:
        by_col.setdefault(c, []).append(r)
    for c, rows in by_col.items():
        if len(rows) == 2 and 0 < c < w-1:
            rows.sort()
            r1, r2 = rows
            for r in range(r1+1, r2):
                res[r][c] = 8 if (r == r1+1 or r == r2-1) else 7
    return res