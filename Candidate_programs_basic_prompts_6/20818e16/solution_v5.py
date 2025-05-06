def solve(grid):
    h=len(grid); w=len(grid[0])
    bg=grid[0][0]
    comps={}
    for i in range(h):
        for j in range(w):
            v=grid[i][j]
            if v!=bg:
                if v not in comps: comps[v]=[i,i,j,j]
                else:
                    comps[v][0]=min(comps[v][0],i)
                    comps[v][1]=max(comps[v][1],i)
                    comps[v][2]=min(comps[v][2],j)
                    comps[v][3]=max(comps[v][3],j)
    outer=max(comps.keys(),key=lambda c:(comps[c][1]-comps[c][0]+1)*(comps[c][3]-comps[c][2]+1))
    y0,y1,x0,x1=comps[outer]
    H=y1-y0+1; W=x1-x0+1
    out=[[outer]*W for _ in range(H)]
    for c,(cy0,cy1,cx0,cx1) in comps.items():
        if c==outer: continue
        dh=cy0-y0; dw=cx0-x0
        for i in range(cy1-cy0+1):
            for j in range(cx1-cx0+1):
                if grid[cy0+i][cx0+j]==c:
                    di=dh+i; dj=dw+j
                    if 0<=di<H and 0<=dj<W:
                        out[di][dj]=c
    return out