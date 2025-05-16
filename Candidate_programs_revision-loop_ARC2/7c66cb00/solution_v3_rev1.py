def solve(grid):
    h, w = len(grid), len(grid[0])
    background = grid[0][0]
    rects_by_color = {}
    for r0 in range(h):
        for c0 in range(w):
            f = grid[r0][c0]
            if not (r0+1<h and c0+1<w and grid[r0][c0+1]==f and grid[r0+1][c0]==f):
                continue
            ce = c0
            while ce+1<w and grid[r0][ce+1]==f:
                ce += 1
            re = r0
            while re+1<h and grid[re+1][c0]==f:
                re += 1
            if re-r0<1 or ce-c0<1:
                continue
            ok = True
            for x in range(c0, ce+1):
                if grid[r0][x]!=f or grid[re][x]!=f:
                    ok = False
                    break
            for y in range(r0, re+1):
                if grid[y][c0]!=f or grid[y][ce]!=f:
                    ok = False
                    break
            if not ok:
                continue
            has_interior = False
            for y in range(r0+1, re):
                for x in range(c0+1, ce):
                    if grid[y][x]!=f:
                        has_interior = True
                        break
                if has_interior:
                    break
            if not has_interior:
                continue
            rects_by_color.setdefault(f, []).append((r0, re, c0, ce))
    out = [[background]*w for _ in range(h)]
    for f, rects in rects_by_color.items():
        for r0, re, c0, ce in rects:
            for x in range(c0, ce+1):
                out[r0][x] = f
                out[re][x] = f
            for y in range(r0, re+1):
                out[y][c0] = f
                out[y][ce] = f
    for f, rects in rects_by_color.items():
        if len(rects)<2:
            r0, re, c0, ce = rects[0]
            for y in range(r0, re+1):
                for x in range(c0, ce+1):
                    out[y][x] = background
            continue
        rects.sort(key=lambda r: (r[1]-r[0])*(r[3]-r[2]))
        r0, re, c0, ce = rects[0]
        pat = [row[c0+1:ce] for row in grid[r0+1:re]]
        ph, pw = len(pat), len(pat[0])
        for y in range(r0, re+1):
            for x in range(c0, ce+1):
                out[y][x] = background
        for x in range(c0, ce+1):
            out[r0][x] = f
            out[re][x] = f
        for y in range(r0, re+1):
            out[y][c0] = f
            out[y][ce] = f
        for r0b, reb, c0b, ceb in rects[1:]:
            for dy in range(ph):
                for dx in range(pw):
                    if pat[dy][dx]!=f:
                        out[r0b+1+dy][c0b+1+dx] = pat[dy][dx]
    return out