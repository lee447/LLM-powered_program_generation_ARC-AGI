def solve(grid):
    m = len(grid)
    n = len(grid[0]) if m else 0
    bottom = next(r for r in range(m - 1, -1, -1) if any(grid[r][c] for c in range(n)))
    stripe_cols = [c for c in range(n) if grid[bottom][c] == 5]
    out = [row[:] for row in grid]
    for c in stripe_cols:
        anchors = sorted((r, grid[r][c]) for r in range(m) if grid[r][c] != 0)
        if not anchors:
            continue
        r0, v0 = anchors[0]
        for r in range(r0 + 1):
            out[r][c] = v0
        for i in range(1, len(anchors)):
            rp, _ = anchors[i - 1]
            rc, vc = anchors[i]
            for r in range(rp + 1, rc + 1):
                out[r][c] = vc
    return out