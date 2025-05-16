def solve(grid):
    h = len(grid)
    w = len(grid[0])
    counts = {}
    for row in grid:
        for v in row:
            counts[v] = counts.get(v, 0) + 1
    items = sorted(counts.items(), key=lambda x: -x[1])
    bg = items[0][0]
    t = next(k for k, _ in items if k != bg)
    row_counts = [row.count(t) for row in grid]
    H = max(range(h), key=lambda r: row_counts[r])
    stripe_cols = []
    for c in range(w):
        cnt = sum(1 for r in range(h) if r != H and grid[r][c] == t)
        if cnt >= 2:
            stripe_cols.append(c)
    out = [[bg]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if r == H:
                if grid[r][c] == t:
                    out[r][c] = t
            else:
                if c in stripe_cols and grid[r][c] == t:
                    out[r][c] = t
    return out