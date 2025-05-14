def solve(grid):
    n = len(grid)
    m = len(grid[0])
    for i in range(1, n-1):
        for j in range(1, m-1):
            if grid[i][j] == 0 and (grid[i-1][j] == 8 or grid[i+1][j] == 8 or grid[i][j-1] == 8 or grid[i][j+1] == 8):
                grid[i][j] = 8
    return grid