def solve(grid):
    h, w = len(grid), len(grid[0])
    background = grid[0][0]
    rects = {}
    for r in range(h - 1):
        for c in range(w - 1):
            f = grid[r][c]
            if f == background: continue
            if grid[r][c + 1] == f and grid[r + 1][c] == f:
                ce = c
                while ce + 1 < w and grid[r][ce + 1] == f:
                    ce += 1
                re = r
                while re + 1 < h and grid[re + 1][c] == f:
                    re += 1
                if re - r < 2 or ce - c < 2: continue
                ok = True
                for x in range(c, ce + 1):
                    if grid[r][x] != f or grid[re][x] != f:
                        ok = False
                        break
                for y in range(r, re + 1):
                    if grid[y][c] != f or grid[y][ce] != f:
                        ok = False
                        break
                if not ok: continue
                rects.setdefault(f, []).append((r, re, c, ce))
    out = [row[:] for row in grid]
    for f, rs in rects.items():
        if len(rs) < 2: continue
        rs.sort(key=lambda x: (x[1] - x[0]) * (x[3] - x[2]))
        r0, r1, c0, c1 = rs[0]
        ph, pw = r1 - r0 - 1, c1 - c0 - 1
        pat = [[grid[r0 + 1 + dy][c0 + 1 + dx] for dx in range(pw)] for dy in range(ph)]
        for y in range(r0, r1 + 1):
            for x in range(c0, c1 + 1):
                out[y][x] = background
        for (ra, rb, ca, cb) in rs[1:]:
            for dy in range(ph):
                for dx in range(pw):
                    v = pat[dy][dx]
                    if v != f:
                        out[ra + 1 + dy][ca + 1 + dx] = v
    return out