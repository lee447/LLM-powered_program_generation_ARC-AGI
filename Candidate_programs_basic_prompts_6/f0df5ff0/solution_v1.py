def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    seeds = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 1]
    out = [row[:] for row in grid]
    for i, j in seeds:
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and out[ni][nj] == 0:
                    out[ni][nj] = 1
    return out