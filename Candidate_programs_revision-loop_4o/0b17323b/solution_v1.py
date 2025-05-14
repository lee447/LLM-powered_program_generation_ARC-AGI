def solve(grid):
    n = len(grid)
    m = len(grid[0])
    result = [row[:] for row in grid]
    color = 1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                for k in range(i, n, 3):
                    for l in range(j, m, 3):
                        if grid[k][l] == 0:
                            result[k][l] = color
                color += 1
    return result