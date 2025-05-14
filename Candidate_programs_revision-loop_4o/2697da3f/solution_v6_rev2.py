def solve(grid):
    n, m = len(grid), len(grid[0])
    new_grid = [[0] * (2 * m - 1) for _ in range(2 * n - 1)]
    for i in range(n):
        for j in range(m):
            new_grid[i][j] = grid[i][j]
            new_grid[i][j + m - 1] = grid[i][j]
            new_grid[i + n - 1][j] = grid[i][j]
            new_grid[i + n - 1][j + m - 1] = grid[i][j]
    return new_grid