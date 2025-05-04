def solve(grid):
    h, w = len(grid), len(grid[0])
    shapes = []
    for r in range(h - 3):
        for c in range(w - 3):
            ok = True
            for rr in (r + 1, r + 2):
                for cc in (c + 1, c + 2):
                    if grid[rr][cc] != 0:
                        ok = False
            for i in range(4):
                if grid[r][c + i] == 0 or grid[r + 3][c + i] == 0 or grid[r + i][c] == 0 or grid[r + i][c + 3] == 0:
                    ok = False
            if ok:
                shapes.append((r, c))
    shapes.sort()
    rows = sorted({r for r, _ in shapes})
    tiers = []
    for r in rows:
        cols = sorted(c for rr, c in shapes if rr == r)
        tiers.append([(r, c) for c in cols])
    palette = [2, 8, 3]
    res = [row[:] for row in grid]
    for ti, tier in enumerate(tiers):
        c1 = palette[ti % 3]
        c2 = palette[(ti + 1) % 3]
        if len(tier) > 0:
            r0, c0 = tier[0]
            for i in range(4):
                res[r0][c0 + i] = c1
                res[r0 + 3][c0 + i] = c1
                res[r0 + i][c0] = c1
                res[r0 + i][c0 + 3] = c1
        if len(tier) > 1:
            r0, c0 = tier[1]
            for i in range(4):
                res[r0][c0 + i] = c2
                res[r0 + 3][c0 + i] = c2
                res[r0 + i][c0] = c2
                res[r0 + i][c0 + 3] = c2
    return res