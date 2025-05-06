def solve(grid):
    H, W = len(grid), len(grid[0])
    pts = [(i, j) for i in range(H) for j in range(W) if grid[i][j] != 0]
    if not pts:
        return grid
    c1 = grid[pts[0][0]][pts[0][1]]
    min_i = min(i for i, _ in pts)
    max_i = max(i for i, _ in pts)
    min_j = min(j for _, j in pts)
    max_j = max(j for _, j in pts)
    h1 = max_i - min_i + 1
    w1 = max_j - min_j + 1
    c2 = 6 if c1 != 6 else 3
    h2, w2 = w1, h1
    step_i, step_j = h1 + h2, w1 + w2
    tl1_i, tl1_j = min_i, min_j
    tl2_i, tl2_j = min_i - h2, min_j - w2
    out = [[0] * W for _ in range(H)]
    start_i1 = tl1_i
    while start_i1 > 0:
        start_i1 -= step_i
    start_j1 = tl1_j
    while start_j1 > 0:
        start_j1 -= step_j
    for i0 in range(start_i1, H, step_i):
        for j0 in range(start_j1, W, step_j):
            for di in range(h1):
                ii = i0 + di
                if 0 <= ii < H:
                    for dj in range(w1):
                        jj = j0 + dj
                        if 0 <= jj < W:
                            out[ii][jj] = c1
    start_i2 = tl2_i
    while start_i2 > 0:
        start_i2 -= step_i
    start_j2 = tl2_j
    while start_j2 > 0:
        start_j2 -= step_j
    for i0 in range(start_i2, H, step_i):
        for j0 in range(start_j2, W, step_j):
            for di in range(h2):
                ii = i0 + di
                if 0 <= ii < H:
                    for dj in range(w2):
                        jj = j0 + dj
                        if 0 <= jj < W:
                            out[ii][jj] = c2
    return out