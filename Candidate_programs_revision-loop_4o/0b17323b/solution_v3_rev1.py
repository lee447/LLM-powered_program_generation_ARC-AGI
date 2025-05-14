def solve(grid):
    n = len(grid)
    m = len(grid[0])
    result = [row[:] for row in grid]
    color = 2
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                for k in range(i + 3, n, 3):
                    for l in range(j + 3, m, 3):
                        if grid[k][l] == 0:
                            result[k][l] = color
                color += 1
    return result