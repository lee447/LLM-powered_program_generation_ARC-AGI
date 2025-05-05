def solve(grid):
    n, m = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    rows = [i for i in range(n) if all(grid[i][j] == 0 for j in range(m))]
    cols = [j for j in range(m) if all(grid[i][j] == 0 for i in range(n))]
    if len(rows) == 2:
        r0, r1 = rows
        d_top = r0
        d_bot = n - r1 - 1
        if d_top >= d_bot:
            c0, c1 = r1 + 1, r1 + 2
        else:
            c0, c1 = n - r1 - 1, n - r1
        for i in range(n):
            if i not in (r0, r1):
                res[i][c0] = 0
                res[i][c1] = 0
        for j in range(m):
            res[r0][j] = 0
            res[r1][j] = 0
    else:
        c0, c1 = cols
        d_left = c0
        d_right = m - c1 - 1
        if d_left >= d_right:
            r0, r1 = c1 + 1, c1 + 2
        else:
            r0, r1 = m - c1 - 1, m - c1
        for j in range(m):
            if j not in (c0, c1):
                res[r0][j] = 0
                res[r1][j] = 0
        for i in range(n):
            res[i][c0] = 0
            res[i][c1] = 0
    return res