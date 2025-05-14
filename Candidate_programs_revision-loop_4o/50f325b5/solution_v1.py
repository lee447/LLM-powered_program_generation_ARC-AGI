def solve(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 3:
                if j + 1 < len(grid[i]) and grid[i][j + 1] == 3:
                    k = j
                    while k < len(grid[i]) and grid[i][k] == 3:
                        grid[i][k] = 8
                        k += 1
                if i + 1 < len(grid) and grid[i + 1][j] == 3:
                    k = i
                    while k < len(grid) and grid[k][j] == 3:
                        grid[k][j] = 8
                        k += 1
    return grid