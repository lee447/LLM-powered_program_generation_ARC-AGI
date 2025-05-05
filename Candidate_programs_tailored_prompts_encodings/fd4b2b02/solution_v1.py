def solve(grid):
    H, W = len(grid), len(grid[0])
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] != 0]
    orig = grid[pts[0][0]][pts[0][1]]
    alt = 3 + 6 - orig
    minr = min(r for r, _ in pts)
    maxr = max(r for r, _ in pts)
    minc = min(c for _, c in pts)
    maxc = max(c for _, c in pts)
    h = maxr - minr + 1
    w = maxc - minc + 1
    motif = [[grid[minr + i][minc + j] for j in range(w)] for i in range(h)]
    rot = [[motif[h - 1 - j][i] for j in range(h)] for i in range(w)]
    out = [[0]*W for _ in range(H)]
    tr = [h, w, h]
    tc = [w, h, w]
    rs = [0, tr[0], tr[0] + tr[1]]
    cs = [0, tc[0], tc[0] + tc[1]]
    for ti in range(3):
        for tj in range(3):
            if ti == 1 and tj == 1: continue
            sr, sc = rs[ti], cs[tj]
            if ti % 2 == 0 and tj % 2 == 0:
                for i in range(h):
                    for j in range(w):
                        if motif[i][j]:
                            rr, cc = sr + i, sc + j
                            if 0 <= rr < H and 0 <= cc < W:
                                out[rr][cc] = orig
            else:
                for i in range(w):
                    for j in range(h):
                        if rot[i][j]:
                            rr, cc = sr + i, sc + j
                            if 0 <= rr < H and 0 <= cc < W:
                                out[rr][cc] = alt
    return out