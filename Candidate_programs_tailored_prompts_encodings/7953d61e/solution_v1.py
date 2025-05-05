def solve(grid):
    n = len(grid)
    m = 2 * n
    out = [[0] * m for _ in range(m)]
    for r in range(n):
        for c in range(n):
            v = grid[r][c]
            out[r][c] = v
            out[n - 1 - c][c + n] = v
            out[n + (n - 1 - r)][n - 1 - c] = v
            out[n + c][n + (n - 1 - r)] = v
    return out