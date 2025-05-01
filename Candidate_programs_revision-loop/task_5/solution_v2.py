def solve(grid):
    h = len(grid)
    w = len(grid[0])
    tile = [[grid[h-1-i][w-1-j] for j in range(w)] for i in range(h)]
    out = [[0] * (2*w) for _ in range(2*h)]
    for i in range(h):
        for j in range(w):
            out[i][j] = tile[i][j]
            out[i][j+w] = tile[i][w-1-j]
            out[i+h][j] = tile[h-1-i][j]
            out[i+h][j+w] = tile[h-1-i][w-1-j]
    return out