def solve(grid):
    h, w = len(grid), len(grid[0])
    flat = [c for row in grid for c in row if c != 0]
    from collections import Counter
    cnt = Counter(flat)
    shape_color = max(cnt, key=lambda k: cnt[k] if k > 0 else -1)
    stripes = []
    for c in range(w):
        col_vals = {grid[r][c] for r in range(h)}
        col_vals.discard(0)
        col_vals.discard(shape_color)
        if col_vals:
            stripes.append((c, col_vals.pop()))
    stripes.sort()
    stripe_cols, stripe_colors = zip(*stripes) if stripes else ([],[])
    out = [[0]*w for _ in range(h)]
    widths = list(stripe_colors)
    for r in range(h):
        xs = [c for c in range(w) if grid[r][c] == shape_color]
        if not xs: continue
        mn, mx = min(xs), max(xs)
        total = mx - mn + 1
        regs = []
        s = 0
        for i, col in enumerate(stripe_cols):
            if i < len(widths)-1:
                w_i = widths[i]
            else:
                w_i = total - s
            regs.append((mn + s, mn + s + w_i - 1, stripe_colors[i]))
            s += w_i
        for lo, hi, col in regs:
            for c in range(lo, hi+1):
                if 0 <= c < w and grid[r][c] == shape_color:
                    out[r][c] = col
    return out