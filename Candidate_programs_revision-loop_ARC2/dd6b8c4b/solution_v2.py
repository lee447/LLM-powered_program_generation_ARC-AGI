def solve(grid):
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    pts = [(i, j) for i in range(h) for j in range(w) if grid[i][j] in (2, 3)]
    if not pts:
        return g
    rs = [i for i, _ in pts]
    cs = [j for _, j in pts]
    r1, r2 = min(rs), max(rs)
    c1, c2 = min(cs), max(cs)
    H1, W1 = r2 - r1 + 1, c2 - c1 + 1
    n9 = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 9]
    if not n9:
        return g
    rs9 = [i for i, _ in n9]
    cs9 = [j for _, j in n9]
    r9min, r9max = min(rs9), max(rs9)
    c9min, c9max = min(cs9), max(cs9)
    H9, W9 = r9max - r9min + 1, c9max - c9min + 1
    for di in range(H1):
        for dj in range(W1):
            i9 = r9min + (di * H9) // H1
            j9 = c9min + (dj * W9) // W1
            if grid[i9][j9] == 9 and g[r1 + di][c1 + dj] != 2:
                g[r1 + di][c1 + dj] = 9
    return g