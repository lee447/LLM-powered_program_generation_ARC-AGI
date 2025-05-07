def solve(grid):
    h = len(grid)
    w = len(grid[0])
    stripes = [(c, grid[0][c]) for c in range(w) if grid[0][c] != 0 and all(grid[r][c] == grid[0][c] for r in range(h))]
    stripes.sort()
    stripe_colors = [v for _, v in stripes]
    stripe_count = len(stripe_colors)
    other = set()
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0 and v not in stripe_colors:
                other.add(v)
    mask_color = other.pop() if other else 0
    min_c, max_c = w, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] == mask_color:
                if c < min_c: min_c = c
                if c > max_c: max_c = c
    width = max_c - min_c
    thresholds = [min_c + width * k / stripe_count for k in range(1, stripe_count)]
    out = [[0] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == mask_color:
                idx = 0
                for t in thresholds:
                    if c > t:
                        idx += 1
                out[r][c] = stripe_colors[idx]
    return out