from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid); w=len(grid[0]); res=[row[:] for row in grid]
    visited=[[False]*w for _ in range(h)]
    dirs=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for r in range(h):
        for c in range(w):
            if grid[r][c]==8 and not visited[r][c]:
                stack=[(r,c)]; visited[r][c]=True
                minr,maxr, minc,maxc=r,r,c,c
                while stack:
                    i,j=stack.pop()
                    if i<minr: minr=i
                    if i>maxr: maxr=i
                    if j<minc: minc=j
                    if j>maxc: maxc=j
                    for di,dj in dirs:
                        ni, nj = i+di, j+dj
                        if 0<=ni<h and 0<=nj<w and not visited[ni][nj] and grid[ni][nj]==8:
                            visited[ni][nj]=True
                            stack.append((ni,nj))
                for i in range(minr, maxr+1):
                    for j in range(minc, maxc+1):
                        if res[i][j]==0:
                            res[i][j]=2
    return res