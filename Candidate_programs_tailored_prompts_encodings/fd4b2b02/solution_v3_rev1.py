def solve(grid):
    H, W = len(grid), len(grid[0])
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] != 0]
    minr = min(r for r, _ in pts)
    maxr = max(r for r, _ in pts)
    minc = min(c for _, c in pts)
    maxc = max(c for _, c in pts)
    h = maxr - minr + 1
    w = maxc - minc + 1
    M = [[grid[minr + i][minc + j] for j in range(w)] for i in range(h)]
    R = [[M[h - 1 - j][i] for j in range(h)] for i in range(w)]
    orig = grid[minr][minc]
    alt = 3 + 6 - orig
    cycle_h = h + w
    cycle_w = w + h
    rs = [0, h, h + w]
    cs = [0, w, w + h]
    out = [row[:] for row in grid]
    ncy = (H + cycle_h - 1) // cycle_h
    ncx = (W + cycle_w - 1) // cycle_w
    for cyc_r in range(ncy):
        for cyc_c in range(ncx):
            base_r = cyc_r * cycle_h
            base_c = cyc_c * cycle_w
            for ti in range(3):
                for tj in range(3):
                    if ti == 1 and tj == 1:
                        continue
                    sr = base_r + rs[ti]
                    sc = base_c + cs[tj]
                    if ti % 2 == 0 and tj % 2 == 0:
                        shape, sh, sw, col = M, h, w, orig
                    else:
                        shape, sh, sw, col = R, w, h, alt
                    for i in range(sh):
                        for j in range(sw):
                            if shape[i][j] != 0:
                                rr = sr + i
                                cc = sc + j
                                if 0 <= rr < H and 0 <= cc < W:
                                    out[rr][cc] = col
    return out