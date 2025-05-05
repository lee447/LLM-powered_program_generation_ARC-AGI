def solve(grid):
    h = len(grid)
    w = len(grid[0])
    mids = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8:
                if j-1 >= 0 and j+1 < w and grid[i][j-1] == 8 and grid[i][j+1] == 8:
                    if not (j-2 >= 0 and grid[i][j-2] == 8) and not (j+2 < w and grid[i][j+2] == 8):
                        mids.append((i, j))
                if i-1 >= 0 and i+1 < h and grid[i-1][j] == 8 and grid[i+1][j] == 8:
                    if not (i-2 >= 0 and grid[i-2][j] == 8) and not (i+2 < h and grid[i+2][j] == 8):
                        mids.append((i, j))
    out = [row[:] for row in grid]
    for i, j in mids:
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                ni, nj = i+di, j+dj
                if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] in (0, 8):
                    out[ni][nj] = 8
    return out