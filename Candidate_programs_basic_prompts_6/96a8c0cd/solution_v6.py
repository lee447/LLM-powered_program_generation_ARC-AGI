def solve(grid):
    h = len(grid)
    w = len(grid[0])
    segs = []
    seen = [[False]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c in (1,3) and not seen[y][x]:
                # horizontal
                if x+2<w and grid[y][x+1]==c and grid[y][x+2]==c and (x-1<0 or grid[y][x-1]!=c):
                    segs.append(('h', y, x, x+2))
                    for xx in (x, x+1, x+2): seen[y][xx] = True
                # vertical
                elif y+2<h and grid[y+1][x]==c and grid[y+2][x]==c and (y-1<0 or grid[y-1][x]!=c):
                    segs.append(('v', x, y, y+2))
                    for yy in (y, y+1, y+2): seen[yy][x] = True
    # find seed
    seed = None
    for y in range(h):
        for x in range(w):
            if grid[y][x]==2:
                seed = (y,x)
                break
        if seed: break
    # compute centers and sort
    centers = []
    for t,a,b,c in segs:
        if t=='h':
            y = a; x = (b+c)//2
        else:
            x = a; y = (b+c)//2
        centers.append((y,x,t,a,b,c))
    centers.sort(key=lambda z:(z[0],z[1]))
    out = [row[:] for row in grid]
    cy,cx = seed
    for y,x,orient,a,b,c in centers:
        opts = []
        if orient=='h':
            x1, x2 = a, c
            if x1-1>=0 and out[y][x1-1]==0: opts.append((y,x1-1))
            if x2+1<w and out[y][x2+1]==0: opts.append((y,x2+1))
        else:
            y1, y2 = b, c
            if y1-1>=0 and out[y1-1][x]==0: opts.append((y1-1,x))
            if y2+1<h and out[y2+1][x]==0: opts.append((y2+1,x))
        if opts:
            tgt = min(opts, key=lambda p:abs(p[0]-cy)+abs(p[1]-cx))
        else:
            tgt = (y,x)
        ty,tx = tgt
        direction = 'h'
        while (cy,cx)!=(ty,tx):
            if direction=='h' and cx!=tx:
                cx += 1 if tx>cx else -1
                if out[cy][cx]==0: out[cy][cx]=2
                direction = 'v'
            elif cy!=ty:
                cy += 1 if ty>cy else -1
                if out[cy][cx]==0: out[cy][cx]=2
                direction = 'h'
            else:
                cx += 1 if tx>cx else -1
                if out[cy][cx]==0: out[cy][cx]=2
                direction = 'v'
        cy,cx = ty,tx
    return out