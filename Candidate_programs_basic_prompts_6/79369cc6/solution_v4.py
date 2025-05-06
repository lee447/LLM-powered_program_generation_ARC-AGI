def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 6:
                if i+1 < h and j-1 >= 0 and grid[i+1][j-1] == 6:
                    if j+1 < w and out[i][j+1] not in (6,4):
                        out[i][j+1] = 4
                    if i+1 < h and j+1 < w and out[i+1][j+1] not in (6,4):
                        out[i+1][j+1] = 4
                if i+1 < h and j+1 < w and grid[i+1][j+1] == 6:
                    if j-1 >= 0 and out[i][j-1] not in (6,4):
                        out[i][j-1] = 4
                    if i+1 < h and j-1 >= 0 and out[i+1][j-1] not in (6,4):
                        out[i+1][j-1] = 4
    return out