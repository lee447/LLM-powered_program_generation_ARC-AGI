def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==5 and not vis[i][j]:
                q=[(i,j)]; vis[i][j]=True; comp=[]
                for x,y in q:
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]==5 and not vis[nx][ny]:
                            vis[nx][ny]=True; q.append((nx,ny))
                rs=[p[0] for p in comp]; cs=[p[1] for p in comp]
                r0,r1=min(rs),max(rs); c0,c1=min(cs),max(cs)
                hole = None
                for y in range(c0,c1+1):
                    if grid[r0][y]==0: hole=(r0,y)
                shapes.append((r0,r1,c0,c1,hole))
    for idx,(r0,r1,c0,c1,(hr,hc)) in enumerate(shapes):
        for i in range(r0+1,r1):
            for j in range(c0+1,c1):
                if grid[i][j]==0:
                    res[i][j]=2
        if grid[hr][hc]==0:
            res[hr][hc]=2
        rr = r0-1 if hr==r0 else (r1+1 if hr==r1 else None)
        if rr is None or not (0<=rr<h): continue
        if (idx%2)==0:
            for j in range(hc, -1, -1):
                if res[rr][j]!=0: break
                res[rr][j]=2
        else:
            for j in range(hc, w):
                if res[rr][j]!=0: break
                res[rr][j]=2
    return res