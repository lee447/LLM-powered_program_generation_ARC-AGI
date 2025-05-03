def solve(grid):
    h=len(grid); w=len(grid[0])
    res=[row[:] for row in grid]
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]>1:
                c=grid[i][j]
                q=[(i,j)]
                vis=[[False]*w for _ in range(h)]
                vis[i][j]=True
                while q:
                    x,y=q.pop()
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]!=1:
                            vis[nx][ny]=True
                            if grid[nx][ny]==0:
                                res[nx][ny]=c
                                q.append((nx,ny))
                            else:
                                q.append((nx,ny))
    return res