def solve(grid):
    h=len(grid); w=len(grid[0])
    g=[row[:] for row in grid]
    vis=[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=1 and not vis[i][j]:
                c=grid[i][j]
                q=[(i,j)]; vis[i][j]=True
                pts=[]
                while q:
                    x,y=q.pop()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny]=True
                            q.append((nx,ny))
                rs=[p[0] for p in pts]; cs=[p[1] for p in pts]
                r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
                bh=r1-r0; bw=maxc-minc
                if len(pts)<=2 or (len(pts)==3 and bh==bw):
                    for x,y in pts: g[x][y]=1
                    cr=(r0+r1)//2; cc=(minc+maxc)//2
                    g[cr][cc]=c
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        x,y=cr+dx,cc+dy
                        if 0<=x<h and 0<=y<w: g[x][y]=c
    return g