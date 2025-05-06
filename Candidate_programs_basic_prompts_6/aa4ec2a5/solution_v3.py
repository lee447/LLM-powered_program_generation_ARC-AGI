def solve(grid):
    H, W = len(grid), len(grid[0])
    vis = [[False]*W for _ in range(H)]
    comps = []
    for y in range(H):
        for x in range(W):
            if grid[y][x]==1 and not vis[y][x]:
                stack = [(x,y)]
                vis[y][x] = True
                cells = []
                while stack:
                    cx, cy = stack.pop()
                    cells.append((cx, cy))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = cx+dx, cy+dy
                        if 0<=nx<W and 0<=ny<H and not vis[ny][nx] and grid[ny][nx]==1:
                            vis[ny][nx] = True
                            stack.append((nx, ny))
                xs = [c[0] for c in cells]
                ys = [c[1] for c in cells]
                comps.append((len(cells), min(xs), max(xs), min(ys), max(ys)))
    areas = sorted({c[0] for c in comps}, reverse=True)
    colmap = {}
    cols = [2,8,6]
    for i,a in enumerate(areas):
        if i<len(cols):
            colmap[a] = cols[i]
    out = [row[:] for row in grid]
    for area, x0, x1, y0, y1 in comps:
        c = colmap.get(area)
        if c is None: continue
        for x in range(x0-1, x1+2):
            if 0<=x<W:
                if 0<=y0-1<H and y0-1>=0 and grid[y0-1][x]==4: out[y0-1][x]=c
                if 0<=y1+1<H and grid[y1+1][x]==4: out[y1+1][x]=c
        for y in range(y0-1, y1+2):
            if 0<=y<H:
                if 0<=x0-1<W and x0-1>=0 and grid[y][x0-1]==4: out[y][x0-1]=c
                if 0<=x1+1<W and grid[y][x1+1]==4: out[y][x1+1]=c
    return out