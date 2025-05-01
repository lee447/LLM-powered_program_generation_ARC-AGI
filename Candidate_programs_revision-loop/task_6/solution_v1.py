def solve(grid):
    H, W = len(grid), len(grid[0])
    cluster_tops = []
    for r in range(H - 1):
        for c in range(W - 1):
            v = grid[r][c]
            if v != 0 and grid[r][c+1] == v and grid[r+1][c] == v and grid[r+1][c+1] == v:
                cluster_tops.append((r, c))
    if not cluster_tops:
        return grid
    r0, c0 = cluster_tops[0]
    sz = 1
    while c0 + sz < W and grid[r0][c0+sz] == grid[r0][c0]:
        sz += 1
    cluster_size = sz
    rows = sorted({r for r, _ in cluster_tops})
    cols = sorted({c for _, c in cluster_tops})
    row_intervals = [(r, r + cluster_size - 1) for r in rows]
    col_intervals = [(c, c + cluster_size - 1) for c in cols]
    min_r = row_intervals[0][0]
    max_r = row_intervals[-1][1]
    min_c = col_intervals[0][0]
    max_c = col_intervals[-1][1]
    stripe_rows = []
    for r in range(min_r, max_r + 1):
        if not any(a <= r <= b for a, b in row_intervals):
            stripe_rows.append(r)
    stripe_cols = []
    for c in range(min_c, max_c + 1):
        if not any(a <= c <= b for a, b in col_intervals):
            stripe_cols.append(c)
    for r in stripe_rows:
        for c in range(W):
            if grid[r][c] == 0:
                grid[r][c] = 2 if min_c <= c <= max_c else 1
    for c in stripe_cols:
        for r in range(H):
            if grid[r][c] == 0:
                grid[r][c] = 2 if min_r <= r <= max_r else 1
    return grid