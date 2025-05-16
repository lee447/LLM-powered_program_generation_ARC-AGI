def solve(grid):
    h = len(grid)
    w = len(grid[0])
    bar = next(x for x in range(w) if all(grid[y][x]==4 for y in range(h)))
    out = [[0]*(bar) for _ in range(h)]
    seen = set()
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c and c!=4:
                seen.add((y,x,c))
    groups = {}
    for y,x,c in seen:
        groups.setdefault((c,y//4), []).append((y,x))
    for (c,b), pts in groups.items():
        xs = [x for _,x in pts]
        ys = [y for y,_ in pts]
        minx,maxx = min(xs), max(xs)
        miny,maxy = min(ys), max(ys)
        wbox = maxx-minx+1
        hbox = maxy-miny+1
        if wbox >= hbox:
            y0 = miny
            for i in range(wbox):
                if 0<=y0<h and 0<=minx+i<bar:
                    out[y0][minx+i] = c
        else:
            x0 = minx
            for i in range(hbox):
                if 0<=miny+i<h and 0<=x0<bar:
                    out[miny+i][x0] = c
    return out