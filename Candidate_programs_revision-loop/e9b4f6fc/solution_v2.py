def solve(grid):
    h, w = len(grid), len(grid[0])
    best = None
    for c in range(1,10):
        coords = [(i,j) for i in range(h) for j in range(w) if grid[i][j]==c]
        if not coords: continue
        ys = [i for i,j in coords]; xs = [j for i,j in coords]
        y0,y1 = min(ys), max(ys); x0,x1 = min(xs), max(xs)
        if y1-y0<1 or x1-x0<1: continue
        ok = True
        for i in range(y0,y1+1):
            for j in range(x0,x1+1):
                if i in (y0,y1) or j in (x0,x1):
                    if grid[i][j]!=c: ok=False
        if ok and (best is None or (y1-y0+1)*(x1-x0+1) > (best[3]-best[2]+1)*(best[1]-best[0]+1)):
            best = (y0,y1,x0,x1,c)
    if not best: return grid
    y0,y1,x0,x1,c = best
    sub = [row[x0:x1+1] for row in grid[y0:y1+1]]
    ih, iw = len(sub), len(sub[0])
    inner = []
    vals = [sub[i][j] for i in range(1,ih-1) for j in range(1,iw-1) if sub[i][j]!=c]
    if vals:
        mx = max(vals)
    else:
        mx = 0
    for i in range(ih):
        row = []
        for j in range(iw):
            v = sub[i][j]
            if i in (0,ih-1) or j in (0,iw-1):
                row.append(v)
            else:
                if v==c:
                    row.append(v)
                else:
                    row.append(mx - v + 1)
        inner.append(row)
    return inner