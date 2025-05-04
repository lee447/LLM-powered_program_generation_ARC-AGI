def solve(grid):
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def flood_fill(r,c, mark):
        stack = [(r,c)]
        cells = [(r,c)]
        vis[r][c] = True
        while stack:
            x,y = stack.pop()
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and g[nx][ny]==3:
                    vis[nx][ny] = True
                    stack.append((nx,ny))
                    cells.append((nx,ny))
        return cells
    rects = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==3 and not vis[i][j]:
                comp = flood_fill(i,j)
                rs = [r for r,c in comp]
                cs = [c for r,c in comp]
                r0,r1 = min(rs), max(rs)
                c0,c1 = min(cs), max(cs)
                if r1-r0>=2 and c1-c0>=2:
                    rects.append((r0,r1,c0,c1))
    for r0,r1,c0,c1 in rects:
        for i in range(r0+1, r1):
            for j in range(c0+1, c1):
                if g[i][j]==0:
                    cnt = 0
                    if g[i-1][j]==3 and g[i+1][j]==3: cnt +=1
                    if g[i][j-1]==3 and g[i][j+1]==3: cnt +=1
                    if cnt>0:
                        g[i][j]=3
    return g