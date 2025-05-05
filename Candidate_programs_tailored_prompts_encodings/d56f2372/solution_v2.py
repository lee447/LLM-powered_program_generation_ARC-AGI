from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H=len(grid); W=len(grid[0])
    visited=[[False]*W for _ in range(H)]
    comps=[]
    for r in range(H):
        for c in range(W):
            if grid[r][c]!=0 and not visited[r][c]:
                val=grid[r][c]
                stack=[(r,c)]
                visited[r][c]=True
                cells=[]
                min_r,max_r,min_c,max_c=r,r,c,c
                while stack:
                    x,y=stack.pop()
                    cells.append((x,y))
                    if x<min_r: min_r=x
                    if x>max_r: max_r=x
                    if y<min_c: min_c=y
                    if y>max_c: max_c=y
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==val:
                            visited[nx][ny]=True
                            stack.append((nx,ny))
                comps.append((min_r,min_c,max_r,max_c,val,cells))
    comps.sort(key=lambda x:(x[0],x[1]))
    min_r,min_c,max_r,max_c,val,cells=comps[0]
    outH=max_r-min_r+1; outW=max_c-min_c+1
    out=[[0]*outW for _ in range(outH)]
    for x,y in cells:
        out[x-min_r][y-min_c]=val
    return out