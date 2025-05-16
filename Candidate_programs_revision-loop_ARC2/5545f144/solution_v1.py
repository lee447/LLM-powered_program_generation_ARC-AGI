def solve(grid):
    h,w=len(grid),len(grid[0])
    def slice_region(col):
        return [[grid[r][c] for c in col] for r in range(h)]
    seps=set()
    for c in range(w):
        colvals={grid[r][c] for r in range(h)}
        if len(colvals)==1 and list(colvals)[0] in (2,3,4):
            seps.add(c)
    cuts=sorted(seps)
    regions=[range(0,cuts[0]), range(cuts[0]+1,cuts[1]), range(cuts[1]+1,w)]
    best=None; bestcnt=0; bestreg=None
    for reg in regions:
        cells=[(r,c) for r in range(h) for c in reg if grid[r][c] not in (0,1,5)]
        if not cells: continue
        color=grid[cells[0][0]][cells[0][1]]
        cnt=len(cells)
        if cnt>bestcnt:
            bestcnt=cnt; best=(reg,color); bestreg=reg
    reg,color=best
    block=slice_region(reg)
    hh,ww=len(block),len(block[0])
    comps=[]
    vis=[[False]*ww for _ in range(hh)]
    for i in range(hh):
        for j in range(ww):
            if block[i][j]==color and not vis[i][j]:
                stack=[(i,j)]; comp=[]
                while stack:
                    x,y=stack.pop()
                    if 0<=x<hh and 0<=y<ww and not vis[x][y] and block[x][y]==color:
                        vis[x][y]=True; comp.append((x,y))
                        stack+=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
                if comp: comps.append(comp)
    comp=max(comps,key=len)
    out=[[block[r][c] for c in range(ww)] for r in range(hh)]
    bg=out[0][0]
    for r in range(hh):
        for c in range(ww):
            out[r][c]=bg
    for x,y in comp:
        out[x][y]=color
    return out