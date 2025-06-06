def solve(grid):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                if j + 1 < cols and grid[i][j + 1] == 0:
                    grid[i][j] = grid[i][j + 1] = 1
                elif i + 1 < rows and grid[i + 1][j] == 0:
                    grid[i][j] = grid[i + 1][j] = 1
    return grid