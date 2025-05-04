def solve(grid):
    H, W = len(grid), len(grid[0])
    anchors = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 4]
    reds = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 2]
    best = None
    best_v = None
    for a in anchors:
        v = sum(abs(r - a[0]) for r, _ in reds)
        if best is None or v < best_v:
            best, best_v = a, v
    ar, ac = best
    offsets = [(r - ar, c - ac) for r, c in reds]
    res = [row[:] for row in grid]
    for r0, c0 in anchors:
        for dr, dc in offsets:
            r, c = r0 + dr, c0 + dc
            if 0 <= r < H and 0 <= c < W and res[r][c] == 0:
                res[r][c] = 2
    return res