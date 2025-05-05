def solve(grid):
    R, C = len(grid), len(grid[0])
    r0 = R; r1 = -1; c0 = C; c1 = -1
    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0:
                r0 = min(r0, i); r1 = max(r1, i)
                c0 = min(c0, j); c1 = max(c1, j)
    h = r1 - r0 + 1; w = c1 - c0 + 1
    oc = grid[r0][c0]
    nc = 3 if oc == 6 else 6
    rh, rw = w, h
    out = [row[:] for row in grid]
    corners = [(0, 0), (0, C - rw), (R - rh, 0), (R - rh, C - rw)]
    edges = [
        (0, (C - w) // 2),
        (R - h, (C - w) // 2),
        ((R - h) // 2, 0),
        ((R - h) // 2, C - w)
    ]
    for dr, dc in corners:
        for i in range(rh):
            for j in range(rw):
                out[dr + i][dc + j] = nc
    for dr, dc in edges:
        for i in range(h):
            for j in range(w):
                out[dr + i][dc + j] = oc
    return out