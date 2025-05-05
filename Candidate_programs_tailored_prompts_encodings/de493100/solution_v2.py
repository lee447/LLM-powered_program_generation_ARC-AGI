def solve(grid):
    H, W = len(grid), len(grid[0])
    rmin = H; rmax = -1; cmin = W; cmax = -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 7:
                rmin = min(rmin, i); rmax = max(rmax, i)
                cmin = min(cmin, j); cmax = max(cmax, j)
    h, w = rmax - rmin + 1, cmax - cmin + 1
    sigs = {}
    for i in range(H - h + 1):
        for j in range(W - w + 1):
            hist = [0]*10
            for ii in range(i, i+h):
                for jj in range(j, j+w):
                    hist[grid[ii][jj]] += 1
            if hist[7] != 0: continue
            sig = tuple(hist)
            sigs.setdefault(sig, []).append((i,j))
    best = None; bestscore = -1
    for sig, lst in sigs.items():
        if len(lst) < 2: continue
        score = sum(sig[v] for v in range(10) if v not in (7,9))
        if score > bestscore:
            bestscore = score; best = lst[0]
    i0, j0 = best
    return [row[j0:j0+w] for row in grid[i0:i0+h]]