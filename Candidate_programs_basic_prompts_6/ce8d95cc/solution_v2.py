def solve(grid):
    H=len(grid); W=len(grid[0])
    bars=[]
    for c in range(1,W-1):
        dl=sum(1 for r in range(H) if grid[r][c]!=grid[r][c-1])
        dr=sum(1 for r in range(H) if grid[r][c]!=grid[r][c+1])
        if dl>=H-2 and dr>=H-2:
            bars.append(c)
    bars.sort()
    segs=[]
    if bars:
        if bars[0]>0: segs.append((0,bars[0]-1))
        for i in range(len(bars)-1):
            a=bars[i]; b=bars[i+1]
            if b-a>1: segs.append((a+1,b-1))
        if bars[-1]<W-1: segs.append((bars[-1]+1,W-1))
    else:
        segs=[(0,W-1)]
    reps=[s for s,e in segs]
    cols=[]
    for i,c in enumerate(bars):
        cols.append(reps[i])
        cols.append(c)
    cols.append(reps[-1])
    stripes=[]
    last=None
    for r in range(H):
        c0=reps[0]
        v=grid[r][c0]
        if r==0 or v!=last:
            stripes.append(r)
            last=v
    out=[]
    for r in stripes:
        out.append([grid[r][c] for c in cols])
    return out