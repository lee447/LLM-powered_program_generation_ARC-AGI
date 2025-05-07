def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    g = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==6 and not vis[i][j]:
                stk = [(i,j)]
                vis[i][j]=True
                comp = [(i,j)]
                while stk:
                    y,x = stk.pop()
                    for dy,dx in dirs:
                        ny,nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx]==6:
                            vis[ny][nx]=True
                            stk.append((ny,nx))
                            comp.append((ny,nx))
                if len(comp)==2:
                    comps.append(comp)
    for comp in comps:
        (r0,c0),(r1,c1) = comp
        dr,dc = r1-r0, c1-c0
        pd = (dc, -dr)
        for (r,c) in comp:
            for mul in (1,2):
                y, x = r + pd[0]*mul, c + pd[1]*mul
                if 0<=y<h and 0<=x<w and grid[y][x]!=6:
                    g[y][x]=4
            for mul in (-1,):
                y, x = r + pd[0]*mul, c + pd[1]*mul
                if 0<=y<h and 0<=x<w and grid[y][x]!=6:
                    g[y][x]=4
    return g