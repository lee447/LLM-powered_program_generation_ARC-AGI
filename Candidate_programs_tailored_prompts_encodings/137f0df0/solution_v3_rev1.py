def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    starts = []
    for i in range(h - 1):
        for j in range(w - 1):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j+1] == grid[i+1][j] == grid[i+1][j+1]:
                starts.append((i, j))
    starts = sorted(starts)
    rows = sorted({i for i, j in starts})
    cols = sorted({j for i, j in starts})
    color = grid[starts[0][0]][starts[0][1]]
    bs = 1
    i0, j0 = starts[0]
    while j0 + bs < w and grid[i0][j0+bs] == color:
        bs += 1
    stripe_rows = []
    for k in range(len(rows) - 1):
        for r in range(rows[k] + bs, rows[k+1]):
            stripe_rows.append(r)
    stripe_cols = []
    for k in range(len(cols) - 1):
        for c in range(cols[k] + bs, cols[k+1]):
            stripe_cols.append(c)
    rmin, rmax = min(rows), max(rows)
    cmin, cmax = min(cols), max(cols)
    for r in stripe_rows:
        for c in range(w):
            if grid[r][c] == 0:
                if c < cmin or c >= cmax + bs:
                    out[r][c] = 1
                else:
                    out[r][c] = 2
    for c in stripe_cols:
        for r in range(h):
            if grid[r][c] == 0:
                if r < rmin or r >= rmax + bs:
                    out[r][c] = 1
                else:
                    out[r][c] = 2
    return out