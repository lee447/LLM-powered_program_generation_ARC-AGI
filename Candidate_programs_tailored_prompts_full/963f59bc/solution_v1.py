def solve(grid):
    h, w = len(grid), len(grid[0])
    blueprint = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    anchors = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] not in (0, 1)]
    min_r = min(r for r, _ in blueprint)
    max_r = max(r for r, _ in blueprint)
    if len(anchors) == 1:
        a1 = a2 = anchors[0]
    else:
        a1 = next(a for a in anchors if min_r <= a[0] <= max_r)
        a2 = next(a for a in anchors if a is not a1)
    fc = a1[2]
    sc = a2[2]
    dx = 1
    while True:
        if all(c+dx < w and grid[r][c+dx] == 0 for r, c in blueprint):
            break
        dx += 1
    dy = None
    r2, c2, _ = a2
    for r0, c0 in blueprint:
        if c0 == c2:
            d = r2 - r0
            if d >= 0 and all(r0p + d < h and (grid[r0p + d][c0p] == 0 or (r0p + d, c0p) == (r2, c2)) for r0p, c0p in blueprint):
                dy = d
                break
    out = [row[:] for row in grid]
    for r, c in blueprint:
        out[r][c+dx] = fc
    for r, c in blueprint:
        out[r+dy][c] = sc
    return out