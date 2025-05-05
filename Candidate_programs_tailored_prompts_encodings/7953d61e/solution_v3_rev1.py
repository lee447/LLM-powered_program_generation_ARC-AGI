def solve(grid):
    n = len(grid)
    m = 2 * n
    out = [[0] * m for _ in range(m)]
    for r in range(n):
        for c in range(n):
            out[r][c] = grid[r][c]
            out[r][n + c] = grid[c][n - 1 - r]
            out[n + r][c] = grid[n - 1 - r][n - 1 - c]
            out[n + r][n + c] = grid[n - 1 - c][r]
    return out