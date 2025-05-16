def solve(grid):
    from collections import Counter
    counts = Counter(c for row in grid for c in row)
    bg = counts.most_common(1)[0][0]
    shape = next(c for c, _ in counts.most_common() if c != bg)
    pts = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == shape]
    minr = min(r for r, _ in pts)
    maxr = max(r for r, _ in pts)
    minc = min(c for _, c in pts)
    maxc = max(c for _, c in pts)
    best_r = max(range(minr, maxr+1), key=lambda r: sum(1 for c in range(minc, maxc+1) if grid[r][c] == shape))
    best_c = max(range(minc, maxc+1), key=lambda c: sum(1 for r in range(minr, maxr+1) if grid[r][c] == shape))
    col_vals = [1 if grid[r][best_c] == shape else 0 for r in range(minr, maxr+1)]
    f = next(i for i, v in enumerate(col_vals) if v)
    l = len(col_vals) - 1 - next(i for i, v in enumerate(reversed(col_vals)) if v)
    segs_r = []
    prev = None
    for v in col_vals[f:l+1]:
        if v != prev:
            segs_r.append(v)
            prev = v
    H = len(segs_r)
    row_vals = [1 if grid[best_r][c] == shape else 0 for c in range(minc, maxc+1)]
    f = next(i for i, v in enumerate(row_vals) if v)
    l = len(row_vals) - 1 - next(i for i, v in enumerate(reversed(row_vals)) if v)
    segs_c = []
    prev = None
    for v in row_vals[f:l+1]:
        if v != prev:
            segs_c.append(v)
            prev = v
    W = len(segs_c)
    out = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            d = min(i, j, H-1-i, W-1-j)
            out[i][j] = shape if d % 2 == 0 else bg
    return out