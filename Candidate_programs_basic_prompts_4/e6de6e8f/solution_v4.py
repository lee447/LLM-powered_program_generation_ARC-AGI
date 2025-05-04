def solve(grid):
    tops = [i for i,v in enumerate(grid[0]) if v==2]
    bots = [i for i,v in enumerate(grid[1]) if v==2]
    m = [sum(1 for t in tops if t < b) for b in bots]
    r = len(bots)
    c = r-1
    out = [[0]*c for _ in range(r)]
    shift = max(0, c - (max(m)+1))
    pts = [(m[i]+shift, i) for i in range(r)]
    x0,y0 = pts[0]
    out[y0][x0] = 3
    for k in range(r-1):
        x1,y1 = pts[k]
        x2,y2 = pts[k+1]
        for x in range(min(x1,x2), max(x1,x2)+1):
            out[y1][x] = 2
            out[y2][x] = 2
        for y in range(min(y1,y2), max(y1,y2)+1):
            out[y][x1] = 2
            out[y][x2] = 2
    return out