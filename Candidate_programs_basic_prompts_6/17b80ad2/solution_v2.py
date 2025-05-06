def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    res = [[0]*w for _ in range(h)]
    for j in range(w):
        seeds = [(i, grid[i][j]) for i in range(h) if grid[i][j] != 0]
        if not seeds:
            continue
        ss = []
        for i, c in seeds:
            if ss and ss[-1][1] == c:
                ss[-1] = (i, c)
            else:
                ss.append((i, c))
        r0, c0 = ss[0]
        for r in range(r0+1):
            res[r][j] = c0
        for k in range(1, len(ss)):
            pr, _ = ss[k-1]
            cr, cc = ss[k]
            for r in range(pr+1, cr+1):
                res[r][j] = cc
    return res