def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 3 and not vis[i][j]:
                q = [(i,j)]
                vis[i][j] = True
                pts = []
                for x,y in q:
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]==3 and not vis[nx][ny]:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                rs = [x for x,_ in pts]; cs = [y for _,y in pts]
                r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
                size = max(r1-r0+1, c1-c0+1)
                comps.append((r0,c0,size))
    comps.sort(key=lambda x: x[0])
    res = [row[:] for row in grid]
    dirs2 = {2: [(0,1),(-1,0)], 3: [(0,1),(1,0),(0,-1)], 1: [(0,1),(-1,0),(0,1),(-1,0)]}[len(comps)]
    cols2 = {2: [1,8], 3: [1,8,1], 1: [1,8,1,8]}[len(comps)]
    for i,(r0,c0,size) in enumerate(comps):
        dr,dc = dirs2[i]
        color = cols2[i]
        nr, nc = r0+dr*(size+2), c0+dc*(size+2)
        for di in range(size):
            for dj in range(size):
                if di in (0,size-1) or dj in (0,size-1):
                    x, y = nr+di, nc+dj
                    if 0<=x<h and 0<=y<w:
                        res[x][y] = color
    return res