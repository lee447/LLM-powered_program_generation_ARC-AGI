def solve(grid):
    h=len(grid);w=len(grid[0])
    pts=[]
    for y in range(h):
        for x in range(w):
            if grid[y][x]==3: pivot=(x,y)
            if grid[y][x] in (1,2): pts.append((x,y))
    for y,x in []: pass
    # normalize stripes to 2
    out=[row[:] for row in grid]
    for y,x in pts:
        out[y][x]=2
    xs=sorted({x for x,y in pts} | {pivot[0]})
    ys=sorted({y for x,y in pts} | {pivot[1]})
    # connect successive x coords at pivot row
    py=pivot[1]
    for i in range(len(xs)-1):
        x1,x2=xs[i],xs[i+1]
        for x in range(x1,x2+1):
            if out[py][x]==8: out[py][x]=3
    # connect successive y coords at pivot col
    px=pivot[0]
    for i in range(len(ys)-1):
        y1,y2=ys[i],ys[i+1]
        for y in range(y1,y2+1):
            if out[y][px]==8: out[y][px]=3
    return out