def solve(grid):
    m = len(grid)
    n = len(grid[0])
    out = [[0] * (2 * n) for _ in range(2 * m)]
    for i in range(2 * m):
        si = m - 1 - i if i < m else i - m
        for j in range(2 * n):
            sj = n - 1 - j if j < n else j - n
            out[i][j] = grid[si][sj]
    return out