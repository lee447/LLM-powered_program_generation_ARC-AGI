def solve(grid):
    h=len(grid); w=len(grid[0])
    cols=[[] for _ in range(w)]
    for r in range(h):
        for c in range(w):
            v=grid[r][c]
            if v!=0:
                cols[c].append((r,v))
    out=[[0]*w for _ in range(h)]
    for c,seeds in enumerate(cols):
        if not seeds: continue
        seeds.sort()
        r0,v0=seeds[0]
        for r in range(r0+1):
            out[r][c]=v0
        for i in range(1,len(seeds)):
            rp,vp=seeds[i]
            for r in range(seeds[i-1][0]+1,rp+1):
                out[r][c]=vp
    return out