def solve(grid):
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == 8 and grid[i][j + 1] != 8:
                grid[i][j + 1] = grid[i + 1][j + 1]
                grid[i][j - 1] = 0
    return grid