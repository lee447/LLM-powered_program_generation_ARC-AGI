def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    vis = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] != 0 and not vis[y][x]:
                col = grid[y][x]
                stack = [(y,x)]
                vis[y][x] = True
                cells = []
                while stack:
                    cy,cx = stack.pop()
                    cells.append((cy,cx))
                    for dy,dx in dirs:
                        ny,nx = cy+dy, cx+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx]==col:
                            vis[ny][nx]=True
                            stack.append((ny,nx))
                ys = [c[0] for c in cells]
                xs = [c[1] for c in cells]
                ymin,ymax = min(ys), max(ys)
                xmin,xmax = min(xs), max(xs)
                comps.append((cells,col,ymin,ymax,xmin,xmax))
    rects, others = [], []
    for cells,col,y0,y1,x0,x1 in comps:
        h0, w0 = y1-y0+1, x1-x0+1
        cnt = len(cells)
        if cnt==h0*w0 or cnt==2*(h0+w0)-4:
            rects.append((cells,col,y0,x0))
        else:
            others.append((cells,col,y0,x0))
    out = [[0]*w for _ in range(h)]
    for cells,col,y0,x0 in rects:
        for y,x in cells:
            out[y-y0][x] = col
    if others:
        mh = max(y1-y0+1 for _,_,y0,y1,x0,x1 in comps if not (len(_)==0))
        base = h-mh
        for cells,col,y0,x0 in others:
            for y,x in cells:
                out[base + (y-y0)][x] = col
    return out