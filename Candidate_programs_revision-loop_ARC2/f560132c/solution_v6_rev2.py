import numpy as np
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h,w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    clusters = {}
    for i in range(h):
        for j in range(w):
            c=grid[i][j]
            if c!=0 and not vis[i][j]:
                pts=[(i,j)]
                vis[i][j]=True
                stk=[(i,j)]
                while stk:
                    x,y=stk.pop()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny]=True
                            pts.append((nx,ny))
                            stk.append((nx,ny))
                clusters.setdefault(c,[]).append(pts)
    for c,comps in clusters.items():
        for pts in comps:
            xs=[x for x,y in pts]; ys=[y for x,y in pts]
            mi,ma=min(xs),max(xs); mj,na=min(ys),max(ys)
            interior=[(i,j,grid[i][j]) for i in range(mi+1,ma) for j in range(mj+1,na)
                      if grid[i][j]!=0 and grid[i][j]!=c]
            if len(interior)==4:
                rows=sorted({i for i,j,_ in interior})
                cols=sorted({j for _,j,_ in interior})
                r0,r1=rows[0],rows[1]; c0,c1=cols[0],cols[1]
                P=[[grid[r0][c0],grid[r0][c1]],[grid[r1][c0],grid[r1][c1]]]
                bh=ma-mi+1; bw=na-mj+1
                scale=min(bh,bw)-1; N=scale*2
                out=[[0]*N for _ in range(N)]
                for i in range(N):
                    for j in range(N):
                        if i+j<=scale:
                            out[i][j]=P[0][0]
                        elif i<scale and j>scale:
                            out[i][j]=P[0][1]
                        elif i>=scale and j<scale:
                            out[i][j]=P[1][0]
                        else:
                            out[i][j]=P[1][1]
                return out
    return []