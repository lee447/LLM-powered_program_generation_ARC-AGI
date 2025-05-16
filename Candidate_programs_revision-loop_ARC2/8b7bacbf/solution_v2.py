def solve(grid):
    h=len(grid); w=len(grid[0])
    counts={}
    for i in range(h):
        for j in range(w):
            v=grid[i][j]
            if v!=0:
                counts[v]=counts.get(v,0)+1
    fill_color=None
    for v,c in counts.items():
        if c==1:
            fill_color=v
            break
    visited=[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==0 and not visited[i][j]:
                q=[(i,j)]; cc=[(i,j)]; visited[i][j]=True
                for x,y in q:
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==0:
                            visited[nx][ny]=True
                            q.append((nx,ny)); cc.append((nx,ny))
                neighbor_colors=set()
                for x,y in cc:
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]!=0 and (nx,ny) not in cc:
                            neighbor_colors.add(grid[nx][ny])
                if len(neighbor_colors)==1:
                    for x,y in cc:
                        grid[x][y]=fill_color
    return grid