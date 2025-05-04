from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid); w=len(grid[0])
    visited=[[False]*w for _ in range(h)]
    dirs=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==8 and not visited[i][j]:
                q=[(i,j)]
                visited[i][j]=True
                cells=[(i,j)]
                mi,mx=i,i
                mj,mxj=j,j
                for x,y in q:
                    for di,dj in dirs:
                        ni,nj=x+di,y+dj
                        if 0<=ni<h and 0<=nj<w and not visited[ni][nj] and grid[ni][nj]==8:
                            visited[ni][nj]=True
                            q.append((ni,nj))
                            cells.append((ni,nj))
                            mi=min(mi,ni); mx=max(mx,ni)
                            mj=min(mj,nj); mxj=max(mxj,nj)
                for r in range(mi,mx+1):
                    for c in range(mj,mxj+1):
                        if grid[r][c]==0:
                            grid[r][c]=2
    return grid