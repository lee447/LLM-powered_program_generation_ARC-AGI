from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    dirs4 = [(1,0),(-1,0),(0,1),(0,-1)]
    def flood(r:int,c:int)->List[Tuple[int,int]]:
        stack=[(r,c)]
        comp=[(r,c)]
        visited[r][c]=True
        while stack:
            x,y=stack.pop()
            for dx,dy in dirs4:
                nx,ny=x+dx,y+dy
                if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==8:
                    visited[nx][ny]=True
                    stack.append((nx,ny))
                    comp.append((nx,ny))
        return comp
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==8 and not visited[i][j]:
                comps.append(flood(i,j))
    for comp in comps:
        rs = [r for r,_ in comp]
        cs = [c for _,c in comp]
        minr, maxr = min(rs), max(rs)
        minc, maxc = min(cs), max(cs)
        for c in range(minc, maxc+1):
            if minr-1>=0 and out[minr-1][c]==0: out[minr-1][c]=2
            if maxr+1<h and out[maxr+1][c]==0: out[maxr+1][c]=2
        for r in range(minr, maxr+1):
            if minc-1>=0 and out[r][minc-1]==0: out[r][minc-1]=2
            if maxc+1<w and out[r][maxc+1]==0: out[r][maxc+1]=2
    for i in range(h-1):
        for j in range(w-1):
            block = [grid[i][j],grid[i+1][j],grid[i][j+1],grid[i+1][j+1]]
            if block.count(8)==3:
                if out[i][j]==0 and grid[i][j]!=8: out[i][j]=2
                if out[i+1][j]==0 and grid[i+1][j]!=8: out[i+1][j]=2
                if out[i][j+1]==0 and grid[i][j+1]!=8: out[i][j+1]=2
                if out[i+1][j+1]==0 and grid[i+1][j+1]!=8: out[i+1][j+1]=2
    return out