def solve(grid):
    n = len(grid)
    m = len(grid[0])
    result = [row[:] for row in grid]
    color = 1
    for j in range(m):
        for i in range(n):
            if grid[i][j] == 1:
                for k in range(i, n, 6):
                    result[k][j] = color
                color += 1
    return result