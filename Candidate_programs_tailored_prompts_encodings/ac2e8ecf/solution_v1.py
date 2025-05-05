def solve(grid):
    h, w = len(grid), len(grid[0])
    rings = []
    for s in (3, 4):
        for i in range(h - s + 1):
            for j in range(w - s + 1):
                c = grid[i][j]
                if c == 0: continue
                ok = True
                for x in range(s):
                    if grid[i][j+x] != c or grid[i+s-1][j+x] != c: ok = False
                    if grid[i+x][j] != c or grid[i+x][j+s-1] != c: ok = False
                if not ok: continue
                for x in range(1, s-1):
                    for y in range(1, s-1):
                        if grid[i+x][j+y] != 0: ok = False
                if ok:
                    rings.append((c, s, i, j))
    keep = []
    bycolor = {}
    for c, s, i, j in rings:
        bycolor.setdefault(c, set()).add(s)
    drop_small = {c for c, ss in bycolor.items() if 3 in ss and 4 in ss}
    for c, s, i, j in rings:
        if c in drop_small and s == 3: continue
        keep.append((c, s, i, j))
    top = sorted([r for r in keep if r[1] == 3], key=lambda x: x[3])
    bot = sorted([r for r in keep if r[1] == 4], key=lambda x: x[3])
    out = [[0]*w for _ in range(h)]
    x = 0
    for c, s, i0, j0 in top:
        for di in range(s):
            for dj in range(s):
                if di in (0, s-1) or dj in (0, s-1):
                    out[di][x+dj] = c
        x += s
    x = 0
    base = h - 4
    for c, s, i0, j0 in bot:
        for di in range(s):
            for dj in range(s):
                if di in (0, s-1) or dj in (0, s-1):
                    out[base+di][x+dj] = c
        x += s
    return out