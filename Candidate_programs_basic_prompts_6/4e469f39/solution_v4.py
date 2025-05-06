def solve(grid):
    h,len_row=len(grid),len(grid[0])
    g=[row[:] for row in grid]
    visited=[[False]*len_row for _ in range(h)]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    comps=[]
    for i in range(h):
        for j in range(len_row):
            if grid[i][j]==5 and not visited[i][j]:
                q=[(i,j)]
                visited[i][j]=True
                comp=[(i,j)]
                for x,y in q:
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<len_row and not visited[nx][ny] and grid[nx][ny]==5:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                comps.append(comp)
    for comp in comps:
        rs=[r for r,_ in comp]; cs=[c for _,c in comp]
        r1,r2,minc,maxc=min(rs),max(rs),min(cs),max(cs)
        for r in range(r1+1,r2):
            for c in range(minc+1,maxc):
                if g[r][c]==0: g[r][c]=2
    return g