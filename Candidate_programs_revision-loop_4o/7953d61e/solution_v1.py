def solve(grid):
    n = len(grid)
    m = len(grid[0])
    result = [[0] * (2 * m) for _ in range(2 * n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = grid[i][j]
            result[i][j + m] = grid[j][i]
            result[i + n][j] = grid[m - j - 1][n - i - 1]
            result[i + n][j + m] = grid[n - i - 1][m - j - 1]
    return result