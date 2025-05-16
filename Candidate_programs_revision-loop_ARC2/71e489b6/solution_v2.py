def solve(grid):
    h=len(grid); w=len(grid[0])
    out=[row[:] for row in grid]
    visited=[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==0 and not visited[i][j]:
                stack=[(i,j)]
                comp=[(i,j)]
                visited[i][j]=True
                while stack:
                    x,y=stack.pop()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==0:
                            visited[nx][ny]=True
                            stack.append((nx,ny))
                            comp.append((nx,ny))
                if len(comp)==1:
                    x,y=comp[0]
                    for dx in (-1,0,1):
                        for dy in (-1,0,1):
                            if dx or dy:
                                nx,ny=x+dx,y+dy
                                if 0<=nx<h and 0<=ny<w:
                                    out[nx][ny]=7
    return out