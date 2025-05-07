def solve(grid):
    h = len(grid)
    w = len(grid[0])
    stripes = []
    for c in range(w):
        v = grid[0][c]
        if v != 0 and all(grid[r][c] == v for r in range(h)):
            stripes.append((c, v))
    stripes.sort()
    stripe_colors = [v for _, v in stripes]
    other = set()
    stripe_set = set(stripe_colors)
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0 and v not in stripe_set:
                other.add(v)
    mask_color = other.pop() if other else 0
    xs = sorted({c for r in range(h) for c in range(w) if grid[r][c] == mask_color})
    runs = []
    start = prev = None
    for x in xs:
        if start is None:
            start = prev = x
        elif x == prev + 1:
            prev = x
        else:
            runs.append((start, prev))
            start = prev = x
    if start is not None:
        runs.append((start, prev))
    out = [[0]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == mask_color:
                for i, (a, b) in enumerate(runs):
                    if a <= c <= b:
                        out[r][c] = stripe_colors[i]
                        break
    return out