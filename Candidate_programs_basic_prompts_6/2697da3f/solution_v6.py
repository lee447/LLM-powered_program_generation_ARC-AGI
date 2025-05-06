def solve(grid):
    H, W = len(grid), len(grid[0])
    col = None
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0:
                col = grid[r][c]
                break
        if col is not None:
            break
    minr, maxr, minc, maxc = H, -1, W, -1
    for r in range(H):
        for c in range(W):
            if grid[r][c] == col:
                if r < minr: minr = r
                if r > maxr: maxr = r
                if c < minc: minc = c
                if c > maxc: maxc = c
    bh, bw = maxr - minr + 1, maxc - minc + 1
    bs = max(bh, bw)
    pad_r = (bs - bh) // 2
    pad_c = (bs - bw) // 2
    shape = [[0] * bs for _ in range(bs)]
    for r in range(bh):
        for c in range(bw):
            shape[pad_r + r][pad_c + c] = grid[minr + r][minc + c]
    overlap = 1 if bs % 2 == 0 else 0
    step = bs - overlap
    T = 3
    out_s = bs * T - overlap
    out = [[0] * out_s for _ in range(out_s)]
    ctr = (T // 2)
    for ti in range(T):
        for tj in range(T):
            drt = ti - ctr
            dct = tj - ctr
            if abs(drt) > abs(dct):
                rot = 2 if drt > 0 else 0
            elif abs(dct) > abs(drt):
                rot = 1 if dct > 0 else 3
            else:
                rot = 0 if drt < 0 else 2 if drt > 0 else 0
            offr = ti * step
            offc = tj * step
            for r in range(bs):
                for c in range(bs):
                    if shape[r][c] == col:
                        rr, cc = r - bs//2, c - bs//2
                        if rot == 1:
                            rr, cc = -cc, rr
                        elif rot == 2:
                            rr, cc = -rr, -cc
                        elif rot == 3:
                            rr, cc = cc, -rr
                        orr = offr + (bs//2 + rr)
                        occ = offc + (bs//2 + cc)
                        out[orr][occ] = col
    return out