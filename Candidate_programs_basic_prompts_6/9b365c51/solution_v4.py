def solve(grid):
    h = len(grid)
    w = len(grid[0])
    counts = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v:
                counts[v] = counts.get(v, 0) + 1
    fill_color = max(counts, key=lambda k: counts[k])
    stripe_positions = []
    stripe_colors = []
    for c in range(w):
        col_vals = set(grid[r][c] for r in range(h) if grid[r][c] != 0)
        if col_vals and col_vals != {fill_color}:
            stripe_positions.append(c)
            vs = [v for v in col_vals if v != fill_color]
            stripe_colors.append(vs[0])
    fill_cols = sorted(c for c in range(w) if any(grid[r][c] == fill_color for r in range(h)))
    intervals = []
    if fill_cols:
        s = fill_cols[0]
        p = s
        for c in fill_cols[1:]:
            if c == p + 1:
                p = c
            else:
                intervals.append((s, p))
                s = c
                p = c
        intervals.append((s, p))
    pairs = sorted(zip(stripe_positions, stripe_colors))
    stripe_colors_sorted = [col for _, col in pairs][:len(intervals)]
    out = [[0] * w for _ in range(h)]
    for i, (s, e) in enumerate(intervals):
        col = stripe_colors_sorted[i]
        for r in range(h):
            for c in range(s, e + 1):
                if grid[r][c] == fill_color:
                    out[r][c] = col
    return out