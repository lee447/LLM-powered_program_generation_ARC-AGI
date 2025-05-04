def solve(grid):
    m,n=len(grid),len(grid[0])
    clusters=[]
    for r in range(m):
        counts={}
        for j,v in enumerate(grid[r]):
            if v:
                counts.setdefault(v,[]).append(j)
        for c,cols in counts.items():
            cols.sort()
            segs=[]
            s=cols[0];p=cols[0]
            for x in cols[1:]:
                if x==p+1:
                    p=x
                else:
                    segs.append((s,p))
                    s=x;p=x
            segs.append((s,p))
            if len(segs)==2 and segs[1][0]-segs[0][1]==2:
                g=segs[0][1]+1
                clusters.append((r,c,segs[0][0],segs[1][1],g))
    clusters.sort(key=lambda x:x[0])
    out=[row[:] for row in grid]
    for r,c,lc,rc,g in clusters:
        for j in range(lc,rc+1):
            out[r][j]=c
        for i in range(r-1,-1,-1):
            if out[i][g]==0:
                out[i][g]=c
            else:
                break
    return out