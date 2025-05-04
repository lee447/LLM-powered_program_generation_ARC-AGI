def solve(grid):
    h, w = len(grid), len(grid[0])
    stripes = []
    for c in range(w):
        vals = [grid[r][c] for r in range(h) if grid[r][c] not in (0, 8)]
        if vals and all(v == vals[0] for v in vals):
            stripes.append((c, vals[0]))
    stripes.sort()
    colors = [color for _, color in stripes]
    coords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
    out = [[0] * w for _ in range(h)]
    if coords and colors:
        xs = [c for _, c in coords]
        mn, mx = min(xs), max(xs)
        width = mx - mn
        k = len(colors)
        if width > 0:
            for r, c in coords:
                p = (c - mn) * k / width
                b = int(p - 1e-6)
                if b < 0: b = 0
                if b >= k: b = k - 1
                out[r][c] = colors[b]
    return out