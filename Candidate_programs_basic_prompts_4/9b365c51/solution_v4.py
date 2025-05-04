def solve(grid):
    H = len(grid)
    W = len(grid[0])
    stripes = []
    for c in range(W):
        col = [grid[r][c] for r in range(H)]
        v = col[0]
        if v != 0 and all(x == v for x in col):
            stripes.append((c, v))
    stripes.sort()
    k = len(stripes)
    stripe_colors = [v for _, v in stripes]
    shape_color = None
    freq = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 0 and v not in stripe_colors:
                freq[v] = freq.get(v, 0) + 1
    if freq:
        shape_color = max(freq, key=freq.get)
    xs = [c for r in range(H) for c in range(W) if grid[r][c] == shape_color]
    if not xs:
        return [[0]*W for _ in range(H)]
    xmin, xmax = min(xs), max(xs)
    if k > 1:
        denom = (xmax - xmin) / (k - 1)
    else:
        denom = 1
    out = [[0]*W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            if grid[r][c] == shape_color:
                if k > 1:
                    idx = int(round((c - xmin) / denom))
                else:
                    idx = 0
                if idx < 0: idx = 0
                if idx >= k: idx = k-1
                out[r][c] = stripe_colors[idx]
    return out