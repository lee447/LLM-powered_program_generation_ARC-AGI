def solve(grid):
    H = len(grid)
    W = len(grid[0])
    pts = [(r, c, grid[r][c]) for r in range(H) for c in range(W) if grid[r][c] != 0]
    pts.sort(key=lambda x: x[0] + x[1])
    out = [row[:] for row in grid]
    used = [[grid[r][c] != 0 for c in range(W)] for r in range(H)]
    def sign(x):
        return (x > 0) - (x < 0)
    n = len(pts)
    if n == 1:
        r, c, v = pts[0]
        mid = (H - 1) / 2
        rr = int(2 * mid - r)
        if 0 <= rr < H:
            for ri in range(min(r, rr) + 1, max(r, rr)):
                out[ri][c] = 5
            out[rr][c] = v
        return out
    for i in range(n - 1):
        r0, c0, v0 = pts[i]
        r1, c1, v1 = pts[i + 1]
        dx = c1 - c0
        dy = r1 - r0
        C = (r0, c1)
        D = (r1, c0)
        # hook from p0 to C
        sx = sign(dx)
        for k in range(1, abs(dx) + 1):
            rr, cc = r0, c0 + k * sx
            if not used[rr][cc]:
                out[rr][cc] = 5
                used[rr][cc] = True
        exr, exc = r0 - sign(dy), c1
        if 0 <= exr < H and 0 <= exc < W and not used[exr][exc]:
            out[exr][exc] = v0
            used[exr][exc] = True
        # hook from p1 to D
        sx = sign(c0 - c1)
        for k in range(1, abs(dx) + 1):
            rr, cc = r1, c1 + k * sx
            if not used[rr][cc]:
                out[rr][cc] = 5
                used[rr][cc] = True
        exr, exc = r1, c0 + sx
        if 0 <= exr < H and 0 <= exc < W and not used[exr][exc]:
            out[exr][exc] = 5
            used[exr][exc] = True
        exr2, exc2 = r1, c0 + 2 * sx
        if 0 <= exr2 < H and 0 <= exc2 < W and not used[exr2][exc2]:
            out[exr2][exc2] = v1
            used[exr2][exc2] = True
    return out