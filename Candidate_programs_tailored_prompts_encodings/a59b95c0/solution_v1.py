def solve(grid):
    n, m = len(grid), len(grid[0])
    k = len({v for row in grid for v in row})
    out = [[0] * (m * k) for _ in range(n * k)]
    for i in range(n * k):
        for j in range(m * k):
            out[i][j] = grid[i % n][j % m]
    return out