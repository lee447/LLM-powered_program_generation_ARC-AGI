def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    greys = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 4]
    rows = {}
    cols = {}
    for r, c in greys:
        rows.setdefault(r, []).append(c)
        cols.setdefault(c, []).append(r)
    for r, clist in rows.items():
        if len(clist) >= 2:
            c0, c1 = sorted(clist)[:2]
            for c in range(c0+1, c1):
                if c == c0+1 or c == c1-1:
                    out[r][c] = 8
                else:
                    out[r][c] = 7
    for c, rlist in cols.items():
        if len(rlist) >= 2:
            r0, r1 = sorted(rlist)[:2]
            for r in range(r0+1, r1):
                if r == r0+1 or r == r1-1:
                    out[r][c] = 8
                else:
                    out[r][c] = 7
    return out