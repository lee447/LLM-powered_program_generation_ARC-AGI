def solve(grid):
    h, w = len(grid), len(grid[0])
    rows = [i for i in range(h) for j in range(w) if grid[i][j] == 8]
    cols = [j for i in range(h) for j in range(w) if grid[i][j] == 8]
    if not rows:
        return [[0] * w for _ in range(h)]
    r0, r1 = min(rows), max(rows)
    c0, c1 = min(cols), max(cols)
    H, W = r1 - r0 + 1, c1 - c0 + 1
    out = [[0] * w for _ in range(h)]
    for y in range(h):
        ry = r0 + ((y - r0) % H)
        for x in range(w):
            cx = c0 + ((x - c0) % W)
            if grid[ry][cx] == 8:
                out[y][x] = 8
    return out