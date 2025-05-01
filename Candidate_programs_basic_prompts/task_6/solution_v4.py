def solve(grid):
    m = len(grid)
    n = len(grid[0])
    res = [row[:] for row in grid]
    xs = [(i, j) for i in range(m) for j in range(n) if grid[i][j] != 0]
    if not xs:
        return res
    rs = [i for i, _ in xs]
    cs = [j for _, j in xs]
    minr, maxr = min(rs), max(rs)
    minc, maxc = min(cs), max(cs)
    internal_rows = [i for i in range(minr + 1, maxr) if all(grid[i][j] == 0 for j in range(n))]
    internal_cols = [j for j in range(minc + 1, maxc) if all(grid[i][j] == 0 for i in range(m))]
    for i in internal_rows:
        for j in range(n):
            if res[i][j] == 0:
                res[i][j] = 2 if minc <= j <= maxc else 1
    for j in internal_cols:
        for i in range(m):
            if res[i][j] == 0:
                res[i][j] = 2 if minr <= i <= maxr else 1
    return res