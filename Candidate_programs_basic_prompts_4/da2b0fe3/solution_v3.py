def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    res = [row[:] for row in grid]
    rows_nz = [any(cell != 0 for cell in grid[r]) for r in range(h)]
    if any(rows_nz):
        rmin, rmax = min(i for i, v in enumerate(rows_nz) if v), max(i for i, v in enumerate(rows_nz) if v)
        for r in range(rmin, rmax + 1):
            if not rows_nz[r]:
                for c in range(w):
                    res[r][c] = 3
                return res
    cols_nz = [any(grid[r][c] != 0 for r in range(h)) for c in range(w)]
    if any(cols_nz):
        cmin, cmax = min(i for i, v in enumerate(cols_nz) if v), max(i for i, v in enumerate(cols_nz) if v)
        for c in range(cmin, cmax + 1):
            if not cols_nz[c]:
                for r in range(h):
                    res[r][c] = 3
                return res
    return res