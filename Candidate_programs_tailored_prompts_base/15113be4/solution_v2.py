def solve(grid):
    H, W = len(grid), len(grid[0])
    sep_rows = [r for r in range(H) if all(grid[r][c] == 4 for c in range(W))]
    sep_cols = [c for c in range(W) if all(grid[r][c] == 4 for r in range(H))]
    sep_rows.sort()
    sep_cols.sort()
    ext_rows = [-1] + sep_rows + [H]
    ext_cols = [-1] + sep_cols + [W]
    row_ranges = [(ext_rows[i] + 1, ext_rows[i+1] - 1) for i in range(len(ext_rows)-1)]
    col_ranges = [(ext_cols[j] + 1, ext_cols[j+1] - 1) for j in range(len(ext_cols)-1)]
    s = None
    dr = dc = None
    for rs, re in row_ranges:
        if s is not None: break
        for cs, ce in col_ranges:
            if s is not None: break
            for r in range(rs, re):
                if s is not None: break
                for c in range(cs, ce):
                    v = grid[r][c]
                    if v not in (0, 1, 4):
                        if grid[r][c+1] == v and grid[r+1][c] == v and grid[r+1][c+1] == v:
                            s = v
                            dr = r - rs
                            dc = c - cs
                            break
    out = [list(row) for row in grid]
    if s is not None:
        for rs, re in row_ranges:
            for cs, ce in col_ranges:
                out[rs+dr][cs+dc] = s
                out[rs+dr+1][cs+dc+1] = s
    return out