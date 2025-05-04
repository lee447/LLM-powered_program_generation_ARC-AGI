def solve(grid):
    H = len(grid)
    W = len(grid[0])
    sep_rows = []
    for i in range(1, H-1):
        v = grid[i][0]
        good = True
        for j in range(1, W):
            if grid[i][j] != v:
                good = False
                break
        if good:
            sep_rows.append(i)
    sep_color = grid[sep_rows[0]][0] if sep_rows else None
    sep_cols = []
    for j in range(1, W-1):
        good = True
        for i in range(H):
            if grid[i][j] != sep_color:
                good = False
                break
        if good:
            sep_cols.append(j)
    counts = {}
    for row in grid:
        for x in row:
            counts[x] = counts.get(x, 0) + 1
    bg = max((c for c in counts if c != sep_color), key=lambda c: counts[c])
    out_h = len(sep_rows) + 1
    out_w = len(sep_cols) + 1
    return [[bg]*out_w for _ in range(out_h)]