def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    clusters = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] and not vis[y][x]:
                c = grid[y][x]
                stack = [(y,x)]
                vis[y][x] = True
                pts = []
                while stack:
                    yy, xx = stack.pop()
                    pts.append((yy,xx))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx]==c:
                            vis[ny][nx] = True
                            stack.append((ny,nx))
                ys = [p[0] for p in pts]
                xs = [p[1] for p in pts]
                y0, y1 = min(ys), max(ys)
                x0, x1 = min(xs), max(xs)
                shape = [[0]*(x1-x0+1) for _ in range(y1-y0+1)]
                for yy,xx in pts:
                    shape[yy-y0][xx-x0] = c
                cx = (y0+y1)/2 - (h-1)/2
                cy = (x0+x1)/2 - (w-1)/2
                ang = -__import__('math').atan2(cx, cy)
                clusters.append((c, pts, y0, x0, y1-y0+1, x1-x0+1, shape, ang, len(pts)))
    small = [c for c in clusters if c[8]==8]
    big = [c for c in clusters if c[8]!=8 and (c[8]==12 or c[8]==(c[4]*2+c[5]*2-4))]
    small.sort(key=lambda c: c[7])
    blk = [[0]*w for _ in range(h)]
    slots = [(0,0),(0,1),(1,1),(1,0)]
    for i,c in enumerate(small):
        _,_,_,_,ch,cw,shape,_,_ = c
        sy,sx = slots[i]
        oy = sy*ch
        ox = sx*cw
        for yy in range(len(shape)):
            for xx in range(len(shape[0])):
                if shape[yy][xx]:
                    blk[oy+yy][ox+xx] = shape[yy][xx]
    if big:
        c = big[0]
        _,_,_,_,ch,cw,shape,_,_ = c
        sy,sx = slots[3]
        oy = sy*ch
        ox = sx*cw
        for yy in range(len(shape)):
            for xx in range(len(shape[0])):
                if shape[yy][xx]:
                    blk[oy+yy][ox+xx] = shape[yy][xx]
    return blk