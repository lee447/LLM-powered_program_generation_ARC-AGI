import numpy as np
def solve(grid):
    H,W=len(grid),len(grid[0])
    vis=[[False]*W for _ in range(H)]
    regions=[]
    for i in range(H):
        for j in range(W):
            if grid[i][j]!=4 and not vis[i][j]:
                comp=[]
                stack=[(i,j)]
                vis[i][j]=True
                while stack:
                    x,y=stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not vis[nx][ny] and grid[nx][ny]!=4:
                            vis[nx][ny]=True
                            stack.append((nx,ny))
                regions.append(comp)
    master_idx=master_color=None
    for idx,comp in enumerate(regions):
        for x,y in comp:
            v=grid[x][y]
            if v not in (0,1,4):
                master_idx,master_color=idx,v
                break
        if master_idx is not None: break
    comp0=regions[master_idx]
    rs=[x for x,y in comp0]; cs=[y for x,y in comp0]
    r0,r1,min_c,max_c=min(rs),max(rs),min(cs),max(cs)
    MH,MW=r1-r0+1,max_c-min_c+1
    mask=[[0]*MW for _ in range(MH)]
    for x,y in comp0:
        if grid[x][y]==master_color:
            mask[x-r0][y-min_c]=1
    out=[row[:] for row in grid]
    for idx,comp in enumerate(regions):
        if idx==master_idx: continue
        vals={grid[x][y] for x,y in comp}
        if not vals.issubset({0,1}): continue
        rs=[x for x,y in comp]; cs=[y for x,y in comp]
        rr0,rr1,cc0,cc1=min(rs),max(rs),min(cs),max(cs)
        h, w=rr1-rr0+1,cc1-cc0+1
        for x,y in comp:
            if grid[x][y]!=1: continue
            ic, jc=x-rr0,y-cc0
            im=ic*MH//h; jm=jc*MW//w
            if mask[im][jm]:
                out[x][y]=master_color
    return out