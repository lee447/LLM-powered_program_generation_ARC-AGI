def solve(grid):
    h, w = len(grid), len(grid[0])
    # find uniform-color rectangles
    regs = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c == grid[0][0] and (i == 0 or j == 0 or i == h-1 or j == w-1):
                continue
            regs.setdefault(c, [h,0,w,0,0])
            r0,r1,c0,c1,_ = regs[c]
            regs[c][0] = min(r0, i)
            regs[c][1] = max(r1, i)
            regs[c][2] = min(c0, j)
            regs[c][3] = max(c1, j)
    cand = []
    for c,(r0,r1,c0,c1,_) in regs.items():
        H = r1-r0+1; W = c1-c0+1
        ok = True
        for i in range(r0,r1+1):
            for j in range(c0,c1+1):
                if grid[i][j] != c:
                    ok = False; break
            if not ok: break
        if ok:
            cand.append((H*W, r0,r1,c0,c1))
    cand.sort()
    _, r0,r1,c0,c1 = cand[0]
    H = r1-r0+1; W = c1-c0+1
    mid = h/2
    if (r0+ r1)/2 < mid:
        # sample below
        out = [[grid[r1+1 + (H-1-i)][c0 + j] for j in range(W)] for i in range(H)]
    else:
        # sample above
        out = [[grid[r0-1 - i][c0 + j] for j in range(W)] for i in range(H)]
    return out