def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = max({c: sum(row.count(c) for row in grid) for c in set(sum(grid, []))}, key=lambda x: {c: sum(row.count(c) for row in grid) for c in set(sum(grid, []))}[x])
    BORDER = 4
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    elbows = []
    for r in range(h):
        for c in range(w):
            if grid[r][c]==BORDER:
                neigh = []
                for dr,dc in dirs:
                    rr,cc = r+dr,c+dc
                    if 0<=rr<h and 0<=cc<w and grid[rr][cc]!=bg and grid[rr][cc]!=BORDER:
                        neigh.append(((dr,dc),grid[rr][cc]))
                if len(neigh)==2 and abs(neigh[0][0][0]*neigh[1][0][0]+neigh[0][0][1]*neigh[1][0][1])==0:
                    elbows.append((r,c,neigh[0],neigh[1]))
    midr, midc = h//2, w//2
    out = [row[:] for row in grid]
    def proc(elb, vertical, horizontal):
        r,c = elb
        drv, dcv, cv = vertical
        drh, dch, ch = horizontal
        vr, vc = r+drv, c+dcv
        hs, ws = r+drh, c+dch
        vrows = []
        rr,cc = vr,vc
        while 0<=rr<h and 0<=cc<w and grid[rr][cc]==cv:
            vrows.append(rr)
            rr += drv; cc += dcv
        hcols = []
        rr,cc = hs,ws
        while 0<=rr<h and 0<=cc<w and grid[rr][cc]==ch:
            hcols.append(cc)
            rr += drh; cc += dch
        if not vrows or not hcols: return
        mnv, mxv = min(vrows), max(vrows)
        mnh, mxh = min(hcols), max(hcols)
        # fill top row only
        r1 = mnv
        for x in range(0, min(vc,c if dcv<0 else c+1)):
            out[r1][x] = BORDER+cv
        # fill intersection row at median of overlap
        overlap = sorted(set(vrows) & set(vrows))
        r2 = vrows[len(vrows)//2]
        for x in range(0, min(vc,c if dcv<0 else c+1)):
            out[r2][x] = cv+ch
        # fill bottom row only
        r3 = mxv
        for x in range(0, min(vc,c if dcv<0 else c+1)):
            out[r3][x] = BORDER-ch
    # top-right quadrant: elbow with neighbors down and left
    trs = [e for e in elbows if e[0]<midr and e[1]>midc]
    for r,c,n1,n2 in trs:
        dirs2 = {n1[0]:n1[1], n2[0]:n2[1]}
        if (1,0) in dirs2 and (0,-1) in dirs2:
            proc((r,c),(1,0,dirs2[(1,0)]),(0,-1,dirs2[(0,-1)]))
    # bottom-left quadrant: elbow with neighbors up and right
    bls = [e for e in elbows if e[0]>midr and e[1]<midc]
    def proc_col(elb, vertical, horizontal):
        r,c = elb
        drv,dcv,cv = vertical
        drh,dch,ch = horizontal
        vr, vc = r+drv, c+dcv
        hs, ws = r+drh, c+dch
        vcols = []
        rr,cc = vr,vc
        while 0<=rr<h and 0<=cc<w and grid[rr][cc]==cv:
            vcols.append(cc)
            rr += drv; cc += dcv
        hrows = []
        rr,cc = hs,ws
        while 0<=rr<h and 0<=cc<w and grid[rr][cc]==ch:
            hrows.append(rr)
            rr += drh; cc += dch
        if not vcols or not hrows: return
        mnh, mxh = min(vcols), max(vcols)
        # leftmost col
        c1 = mnh
        for y in range(min(hs,r if drh<0 else r+1), min(hs,r if drh<0 else r+1)+len(hrows)):
            out[y][c1] = BORDER+ch
        # middle col
        c2 = vcols[len(vcols)//2]
        for y in range(min(hs,r if drh<0 else r+1), min(hs,r if drh<0 else r+1)+len(hrows)):
            out[y][c2] = cv+ch
        # rightmost col
        c3 = mxh
        for y in range(min(hs,r if drh<0 else r+1), min(hs,r if drh<0 else r+1)+len(hrows)):
            out[y][c3] = BORDER-cv
    for r,c,n1,n2 in bls:
        dirs2 = {n1[0]:n1[1], n2[0]:n2[1]}
        if (-1,0) in dirs2 and (0,1) in dirs2:
            proc_col((r,c),(-1,0,dirs2[(-1,0)]),(0,1,dirs2[(0,1)]))
    return out