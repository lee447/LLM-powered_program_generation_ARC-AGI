def solve(grid):
    n = len(grid)
    m = len(grid[0])
    result = [row[:] for row in grid]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                color = 2
                for k in range(i + 3, n, 3):
                    if grid[k][j] == 0:
                        result[k][j] = color
                color += 1
    return result