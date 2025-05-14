def solve(grid):
    n = len(grid)
    m = len(grid[0])
    new_grid = [row[:] for row in grid]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if grid[i][j] == 8:
                if grid[i-1][j] == 8 and grid[i+1][j] == 8:
                    new_grid[i][j] = 0
                elif grid[i][j-1] == 8 and grid[i][j+1] == 8:
                    new_grid[i][j] = 0
    return new_grid