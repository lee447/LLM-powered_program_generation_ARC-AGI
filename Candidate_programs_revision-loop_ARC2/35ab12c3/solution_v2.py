def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    vis = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] and not vis[y][x]:
                c = grid[y][x]
                stk = [(y,x)]
                comp = []
                vis[y][x] = True
                while stk:
                    yy, xx = stk.pop()
                    comp.append((yy,xx))
                    for dy,dx in dirs:
                        ny, nx = yy+dy, xx+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx]==c:
                            vis[ny][nx]=True
                            stk.append((ny,nx))
                comps.append((c, comp))
    out = [row[:] for row in grid]
    for c, comp in comps:
        if c==3: continue
        ys = [p[0] for p in comp]
        xs = [p[1] for p in comp]
        y0, y1 = min(ys), max(ys)
        x0, x1 = min(xs), max(xs)
        if len(comp)==2:
            c1 = grid[comp[0][0]][comp[0][1]]
            c2 = grid[comp[1][0]][comp[1][1]]
            midy = min(ys)
            length = midy
            for d in range(0, length+1):
                row = midy - d
                for dx in range(d+1):
                    for sign in (-1,1):
                        x = comp[0][1] + sign*dx
                        if 0<=row<h and 0<=x<w:
                            out[row][x] = c1 if d%2==0 else c2
        else:
            for x in range(x0, x1+1):
                out[y0][x]=c
                out[y1][x]=c
            for y in range(y0, y1+1):
                out[y][x0]=c
                out[y][x1]=c
    return out