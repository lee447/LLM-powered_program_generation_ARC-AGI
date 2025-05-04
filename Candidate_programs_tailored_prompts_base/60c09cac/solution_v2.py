def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [[0] * (2 * w) for _ in range(2 * h)]
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            out[2*i][2*j] = c
            out[2*i][2*j+1] = c
            out[2*i+1][2*j] = c
            out[2*i+1][2*j+1] = c
    return out