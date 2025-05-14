def solve(grid):
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j + 1] == grid[i][j + 2] == grid[i][j + 3]:
                grid[i][j + 2] = grid[i][j + 3] = grid[i][j + 4] = 0
    return grid