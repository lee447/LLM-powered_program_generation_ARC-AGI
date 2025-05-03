from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid); w=len(grid[0])
    vis=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not vis[i][j]:
                stack=[(i,j)]; vis[i][j]=True; comp=[]
                while stack:
                    r,c=stack.pop()
                    comp.append((r,c,grid[r][c]))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not vis[nr][nc] and grid[nr][nc]!=0:
                            vis[nr][nc]=True
                            stack.append((nr,nc))
                comps.append(comp)
    mins=sorted({min(r for r,_,_ in comp) for comp in comps})
    offsets=[0,-1,0,1]
    out=[[0]*w for _ in range(h)]
    for comp in comps:
        r0=min(r for r,_,_ in comp)
        off=offsets[mins.index(r0)%len(offsets)]
        for r,c,v in comp:
            out[r][c+off]=v
    return out