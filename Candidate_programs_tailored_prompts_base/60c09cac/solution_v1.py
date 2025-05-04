def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    out = [[0] * (2 * w) for _ in range(2 * h)]
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c:
                ii, jj = 2 * i, 2 * j
                out[ii][jj] = c
                out[ii][jj + 1] = c
                out[ii + 1][jj] = c
                out[ii + 1][jj + 1] = c
    return out