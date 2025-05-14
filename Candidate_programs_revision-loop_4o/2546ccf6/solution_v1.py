def solve(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                if i > 0 and grid[i-1][j] != 0:
                    grid[i][j] = grid[i-1][j]
                elif j > 0 and grid[i][j-1] != 0:
                    grid[i][j] = grid[i][j-1]
    return grid