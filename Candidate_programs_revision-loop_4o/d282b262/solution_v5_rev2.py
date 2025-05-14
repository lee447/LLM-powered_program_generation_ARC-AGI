def solve(grid):
    n = len(grid)
    m = len(grid[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                result[j][m - i - 1] = grid[i][j]
    return result