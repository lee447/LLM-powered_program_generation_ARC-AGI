def solve(grid):
    H, W = len(grid), len(grid[0])
    anchors = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 4]
    reds = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 2]
    best = min(anchors, key=lambda a: sum(abs(r - a[0]) + abs(c - a[1]) for r, c in reds))
    ar, ac = best
    offsets = [(r - ar, c - ac) for r, c in reds]
    res = [row[:] for row in grid]
    for r0, c0 in anchors:
        vs = 1 if r0 >= ar else -1
        hs = -1
        cells = [(r0 + dr * vs, c0 + dc * hs) for dr, dc in offsets]
        if all(0 <= r < H and 0 <= c < W and res[r][c] == 0 for r, c in cells):
            for r, c in cells:
                res[r][c] = 2
    return res