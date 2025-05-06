def solve(grid):
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    orig = [row[:] for row in grid]
    colors = sorted({c for row in grid for c in row if c != 0}, key=lambda c: min(r for r,row in enumerate(grid) for x in row if x==c))
    for c in colors:
        pts = [(r,x) for r,row in enumerate(orig) for x,v in enumerate(row) if v==c]
        rows = sorted({r for r,_ in pts})
        cols = sorted({x for _,x in pts})
        r = rows[0] if len(rows)==1 else None
        cc = cols[0] if len(cols)==1 else None
        if r is not None:
            cols_here = [x for _,x in pts]
            minc, maxc = min(cols_here), max(cols_here)
            for x in range(minc, maxc+1):
                res[r][x] = c
        if cc is not None:
            rows_here = [r for r,_ in pts]
            minr, maxr = min(rows_here), max(rows_here)
            for y in range(minr, maxr+1):
                res[y][cc] = c
        if r is not None and cc is None:
            # count horizontal segments
            segs = 0
            for x in range(w):
                if orig[r][x]==c and (x==0 or orig[r][x-1]!=c):
                    segs += 1
            if segs > 1:
                # find gap
                minc, maxc = min(x for _,x in pts), max(x for _,x in pts)
                gap = next(x for x in range(minc, maxc+1) if orig[r][x]==0)
                for y in range(r-1, -1, -1):
                    if res[y][gap] != 0: break
                    res[y][gap] = c
        if cc is not None and r is None:
            segs = 0
            for y in range(h):
                if orig[y][cc]==c and (y==0 or orig[y-1][cc]!=c):
                    segs += 1
            if segs > 1:
                minr, maxr = min(r for r,_ in pts), max(r for r,_ in pts)
                gap = next(y for y in range(minr, maxr+1) if orig[y][cc]==0)
                for x in range(cc-1, -1, -1):
                    if res[gap][x] != 0: break
                    res[gap][x] = c
    return res