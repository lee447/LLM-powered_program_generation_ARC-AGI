def solve(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                if j + 1 < len(grid[i]) and grid[i][j + 1] == 0:
                    grid[i][j] = grid[i][j + 1] = 6
                elif i + 1 < len(grid) and grid[i + 1][j] == 0:
                    grid[i][j] = grid[i + 1][j] = 3
    return grid