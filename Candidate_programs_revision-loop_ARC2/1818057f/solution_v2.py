def solve(grid):
    h = len(grid)
    w = len(grid[0])
    centers = []
    for i in range(1, h-1):
        for j in range(1, w-1):
            if grid[i][j] == 4 and grid[i-1][j] == 4 and grid[i+1][j] == 4 and grid[i][j-1] == 4 and grid[i][j+1] == 4:
                centers.append((i, j))
    out = [row[:] for row in grid]
    for i, j in centers:
        out[i][j] = 8
        out[i-1][j] = 8
        out[i+1][j] = 8
        out[i][j-1] = 8
        out[i][j+1] = 8
    return out