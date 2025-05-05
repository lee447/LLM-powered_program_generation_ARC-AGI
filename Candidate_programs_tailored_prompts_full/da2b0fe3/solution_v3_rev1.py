import math
def solve(grid):
    h, w = len(grid), len(grid[0])
    nonzeros = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    if not nonzeros:
        return grid
    rs = [r for r, _ in nonzeros]
    cs = [c for _, c in nonzeros]
    min_r, max_r = min(rs), max(rs)
    min_c, max_c = min(cs), max(cs)
    row_span = max_r - min_r
    col_span = max_c - min_c
    res = [row[:] for row in grid]
    if row_span >= col_span:
        axis_row = int((min_r + max_r) / 2 + 0.5)
        res[axis_row] = [3] * w
    else:
        axis_col = int((min_c + max_c) / 2 + 0.5)
        for r in range(h):
            res[r][axis_col] = 3
    return res