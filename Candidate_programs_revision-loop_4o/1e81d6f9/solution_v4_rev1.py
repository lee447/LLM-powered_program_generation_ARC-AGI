def solve(grid):
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 0:
                for k in range(i - 1, -1, -1):
                    if grid[k][j] != 0:
                        grid[i][j] = grid[k][j]
                        break
    return grid