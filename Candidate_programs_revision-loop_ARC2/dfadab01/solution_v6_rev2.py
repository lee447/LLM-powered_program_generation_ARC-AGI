def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [[0]*w for _ in range(h)]
    pos = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v > 0:
                pos.setdefault(v, []).append((r, c))
    def draw_hollow(r0, c0, col):
        for i in range(4):
            out[r0+i][c0] = col
            out[r0+i][c0+3] = col
            out[r0][c0+i] = col
            out[r0+3][c0+i] = col
    def draw_square2(r0, c0):
        for dr in (0, 2):
            for dc in (0, 2):
                for i in range(2):
                    for j in range(2):
                        out[r0+dr+i][c0+dc+j] = 6
    diag = [(0,1),(0,2),(1,0),(1,3),(2,0),(2,3),(3,1),(3,2)]
    for v in (2, 3, 5, 8):
        if v in pos:
            for r0, c0 in pos[v]:
                if r0+3 < h and c0+3 < w:
                    ok = True
                    for dr in range(4):
                        for dc in range(4):
                            if not (dr == 0 and dc == 0) and grid[r0+dr][c0+dc] != 0:
                                ok = False
                                break
                        if not ok:
                            break
                    if not ok:
                        continue
                    if v == 2:
                        draw_hollow(r0, c0, 4)
                    elif v == 3:
                        draw_hollow(r0, c0, 1)
                    elif v == 5:
                        draw_square2(r0, c0)
                    else:
                        for dr, dc in diag:
                            out[r0+dr][c0+dc] = 7
    if 1 in pos:
        pts = pos[1][:]
        clusters = []
        while pts:
            cr, cc = pts.pop(0)
            cl = [(cr, cc)]
            changed = True
            while changed:
                changed = False
                for r, c in pts[:]:
                    if any(abs(r - ar) <= 3 and abs(c - ac) <= 3 for ar, ac in cl):
                        cl.append((r, c))
                        pts.remove((r, c))
                        changed = True
            clusters.append(cl)
        for cl in clusters:
            r0 = min(r for r, c in cl)
            c0 = min(c for r, c in cl)
            for dr, dc in diag:
                out[r0+dr][c0+dc] = 1
    return out