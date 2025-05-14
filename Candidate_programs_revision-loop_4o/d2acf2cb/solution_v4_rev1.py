def solve(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 4:
                if i > 0 and grid[i-1][j] == 0:
                    grid[i-1][j] = 8
                if i < len(grid) - 1 and grid[i+1][j] == 0:
                    grid[i+1][j] = 8
                if j > 0 and grid[i][j-1] == 0:
                    grid[i][j-1] = 8
                if j < len(grid[i]) - 1 and grid[i][j+1] == 0:
                    grid[i][j+1] = 8

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 8:
                if i > 0 and grid[i-1][j] == 0:
                    grid[i-1][j] = 7
                if i < len(grid) - 1 and grid[i+1][j] == 0:
                    grid[i+1][j] = 7
                if j > 0 and grid[i][j-1] == 0:
                    grid[i][j-1] = 7
                if j < len(grid[i]) - 1 and grid[i][j+1] == 0:
                    grid[i][j+1] = 7

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 8:
                grid[i][j] = 0

    return grid