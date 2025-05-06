def solve(grid):
    h, w = len(grid), len(grid[0])
    bs = sorted({c for row in grid for c in row if c not in (0,1,4)})
    c = bs[0] if bs else None
    rows = [i for i in range(h) if all(grid[i][j]==4 for j in range(w))]
    cols = [j for j in range(w) if all(grid[i][j]==4 for i in range(h))]
    br = [(-1,)+tuple(rows)+ (h,)]
    bc = [(-1,)+tuple(cols)+(w,)]
    vr = [(rows[i]+1, rows[i+1]) for i in range(len(rows)+0)]
    vc = [(cols[j]+1, cols[j+1]) for j in range(len(cols)+0)]
    out = [row[:] for row in grid]
    for bi, (r0,r1) in enumerate(vr):
        for bj, (c0,c1) in enumerate(vc):
            block = [grid[i][c0:c1] for i in range(r0,r1)]
            cnt0 = sum(v==0 for row in block for v in row)
            cnt1 = sum(v==1 for row in block for v in row)
            if cnt1<cnt0:
                for i in range(r0,r1):
                    for j in range(c0,c1):
                        if grid[i][j]==1:
                            out[i][j]=c
    return out