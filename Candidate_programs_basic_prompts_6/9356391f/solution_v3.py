def solve(grid):
    rows=len(grid)
    cols=len(grid[0])
    pr=pc=None
    for i in range(2,rows):
        for j in range(cols):
            if grid[i][j]!=0:
                pr,pc=i,j
                break
        if pr is not None:
            break
    row0=grid[0]
    segs=[]
    cur_start=0
    cur_nonzero=row0[0]!=0
    for i in range(1,cols):
        nz=row0[i]!=0
        if nz!=cur_nonzero:
            segs.append((cur_start,i,cur_nonzero,row0[cur_start:i]))
            cur_start=i
            cur_nonzero=nz
    segs.append((cur_start,cols,cur_nonzero,row0[cur_start:cols]))
    pidx=0
    for idx,(s,e,_,_) in enumerate(segs):
        if s<=pc<e:
            pidx=idx
            break
    rings=[]
    for idx in range(pidx,-1,-1):
        s,e,nonzero,vals=segs[idx]
        if nonzero:
            for c in reversed(vals):
                rings.append(c)
        else:
            rings.append(0)
    dmax=len(rings)-1
    out=[row[:] for row in grid]
    if dmax>=0:
        for r in range(rows):
            for c in range(cols):
                d=max(abs(r-pr),abs(c-pc))
                if d<=dmax:
                    out[r][c]=rings[dmax-d]
    return out