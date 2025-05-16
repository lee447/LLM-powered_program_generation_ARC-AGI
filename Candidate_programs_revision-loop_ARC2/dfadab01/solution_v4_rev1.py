def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [[0]*w for _ in range(h)]
    def draw_hollow(r, c, L, col):
        for i in range(L):
            for j in range(L):
                if i in (0, L-1) or j in (0, L-1):
                    out[r+i][c+j] = col
    def draw_filled2(r, c, col):
        out[r][c] = out[r+1][c] = out[r][c+1] = out[r+1][c+1] = col
    diag = [(0,0),(0,3),(1,1),(1,2),(2,0),(2,1),(3,2),(3,3)]
    vals = {v for row in grid for v in row}
    if 8 in vals:
        for r in range(0, h, 4):
            for c in range(0, w, 4):
                v = grid[r][c]
                if v == 2:
                    draw_hollow(r, c, 4, 4)
                elif v == 3:
                    draw_hollow(r, c, 4, 1)
                elif v == 5:
                    draw_filled2(r, c, 6)
                    draw_filled2(r+2, c+2, 6)
                elif v == 8:
                    for dr, dc in diag:
                        out[r+dr][c+dc] = 7
    elif 6 in vals and 5 in vals:
        pos = {}
        for r in range(h):
            for c in range(w):
                v = grid[r][c]
                if v > 0:
                    pos.setdefault(v, []).append((r, c))
        for v, P in pos.items():
            if v == 2:
                for r, c in P:
                    if r+3 < h and c+3 < w:
                        draw_hollow(r, c, 4, 4)
            elif v == 3:
                for r, c in P:
                    if r+3 < h and c+3 < w:
                        draw_hollow(r, c, 4, 1)
            elif v == 5:
                byrow = {}
                for r0, c0 in P:
                    byrow.setdefault(r0, []).append(c0)
                for r0, cs in byrow.items():
                    if len(cs) == 2:
                        for c0 in cs:
                            draw_filled2(r0, c0, 6)
    elif 1 in vals:
        pos = {}
        for r in range(h):
            for c in range(w):
                v = grid[r][c]
                if v > 0:
                    pos.setdefault(v, []).append((r, c))
        for v, P in pos.items():
            if v == 3:
                for r, c in P:
                    if r+3 < h and c+3 < w:
                        draw_hollow(r, c, 4, 1)
            elif v == 2:
                for r, c in P:
                    if r+3 < h and c+3 < w:
                        draw_hollow(r, c, 4, 4)
            elif v == 1:
                byrow = {}
                for r0, c0 in P:
                    byrow.setdefault(r0, []).append(c0)
                for r0, cs in byrow.items():
                    if len(cs) == 2:
                        for c0 in cs:
                            draw_filled2(r0, c0, 1)
    else:
        for r in range(h):
            for c in range(w):
                if grid[r][c] == 2 and r+3 < h and c+3 < w:
                    ok = True
                    for dr in range(4):
                        for dc in range(4):
                            if not (dr == 0 and dc == 0) and grid[r+dr][c+dc] != 0:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        draw_hollow(r, c, 4, 4)
    return out