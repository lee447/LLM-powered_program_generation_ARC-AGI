def solve(grid):
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 5:
                if i > 0 and grid[i-1][j] == 0:
                    grid[i-1][j] = 1
                if i < len(grid) - 1 and grid[i+1][j] == 0:
                    grid[i+1][j] = 2
                if j > 0 and grid[i][j-1] == 0:
                    grid[i][j-1] = 3
                if j < len(row) - 1 and grid[i][j+1] == 0:
                    grid[i][j+1] = 4
    return grid