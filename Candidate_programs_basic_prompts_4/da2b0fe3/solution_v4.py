def solve(grid: list[list[int]]) -> list[list[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    row_has = [any(cell != 0 for cell in grid[r]) for r in range(h)]
    nonzero_rows = [r for r, v in enumerate(row_has) if v]
    if nonzero_rows:
        rmin, rmax = min(nonzero_rows), max(nonzero_rows)
    else:
        rmin, rmax = 0, -1
    blank_rows = [r for r in range(rmin + 1, rmax) if not row_has[r]]
    if blank_rows:
        for r in blank_rows:
            grid[r] = [3] * w
        return grid
    col_has = [any(grid[r][c] != 0 for r in range(h)) for c in range(w)]
    nonzero_cols = [c for c, v in enumerate(col_has) if v]
    if nonzero_cols:
        cmin, cmax = min(nonzero_cols), max(nonzero_cols)
    else:
        cmin, cmax = 0, -1
    blank_cols = [c for c in range(cmin + 1, cmax) if not col_has[c]]
    for c in blank_cols:
        for r in range(h):
            grid[r][c] = 3
    return grid