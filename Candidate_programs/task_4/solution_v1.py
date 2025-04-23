from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h=len(grid);w=len(grid[0])
    bg=grid[0][0]
    vis=[[False]*w for _ in range(h)]
    shapes=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=bg and not vis[i][j]:
                col=grid[i][j]
                pts=[]
                stack=[(i,j)]
                vis[i][j]=True
                while stack:
                    x,y=stack.pop()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==col:
                            vis[nx][ny]=True
                            stack.append((nx,ny))
                mr=min(x for x,y in pts)
                mc=min(y for x,y in pts)
                shapes.append((mr,mc,col,pts))
    shapes.sort(key=lambda x:(x[0],x[1]))
    out=[[bg]*w for _ in range(h)]
    for idx,(mr,mc,col,pts) in enumerate(shapes):
        shift = -1 if idx%2==0 else 1
        for x,y in pts:
            out[x][y+shift]=col
    return out