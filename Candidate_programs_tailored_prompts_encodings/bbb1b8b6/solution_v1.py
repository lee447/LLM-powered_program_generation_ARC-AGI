def solve(grid):
    nrows = len(grid)
    ncols = len(grid[0])
    col5 = next(j for j in range(ncols) if any(grid[i][j] == 5 for i in range(nrows)))
    w_left = col5
    w_right = ncols - col5 - 1
    w = w_left
    left = {}
    for i in range(nrows):
        for j in range(w_left):
            v = grid[i][j]
            if v != 0:
                left[(i, j)] = v
    right = {}
    for i in range(nrows):
        for j in range(col5 + 1, ncols):
            v = grid[i][j]
            if v != 0:
                right[(i, j - col5 - 1)] = v
    collision = any(pos in left for pos in right)
    out = [[0] * w for _ in range(nrows)]
    if collision:
        for (i, j), v in left.items():
            out[i][j] = v
    else:
        for (i, j), v in right.items():
            out[i][j] = v
        for (i, j), v in left.items():
            out[i][j] = v
    return out