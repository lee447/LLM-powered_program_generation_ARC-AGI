def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [[0] * (w * 2) for _ in range(h * 2)]
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            r, c = i * 2, j * 2
            out[r][c] = v
            out[r][c+1] = v
            out[r+1][c] = v
            out[r+1][c+1] = v
    return out