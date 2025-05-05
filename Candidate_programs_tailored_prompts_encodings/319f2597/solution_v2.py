def solve(grid):
    n = len(grid)
    m = len(grid[0])
    res = [row[:] for row in grid]
    zeros = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 0]
    rows = sorted({i for i, _ in zeros})
    cols = sorted({j for _, j in zeros})
    r0, r1 = rows[0], rows[1]
    c0, c1 = cols[0], cols[1]
    midc = (c0 + c1) / 2
    if n / 3 <= midc <= 2 * n / 3:
        for c in range(m):
            res[r0][c] = 0
            res[r1][c] = 0
    else:
        for r in range(n):
            res[r][c0] = 0
            res[r][c1] = 0
    return res