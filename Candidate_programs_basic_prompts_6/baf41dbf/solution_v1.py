def solve(grid):
    h=len(grid);w=len(grid[0])
    coords3=[(y,x) for y in range(h) for x in range(w) if grid[y][x]==3]
    ys=[y for y,x in coords3]; xs=[x for y,x in coords3]
    oy,by=min(ys),max(ys); ox,bx=min(xs),max(xs)
    bxmin, bxmax, bymin, bymax = ox, bx, oy, by
    for y in range(h):
        for x in range(w):
            if grid[y][x]==6:
                if oy<=y<=by:
                    if x<ox: bxmin=min(bxmin,x+1)
                    if x>bx: bxmax=max(bxmax,x-1)
                if ox<=x<=bx:
                    if y<oy: bymin=min(bymin,y+1)
                    if y>by: bymax=max(bymax,y-1)
    out=[row[:] for row in grid]
    for x in range(bxmin,bxmax+1):
        if out[bymin][x]!=6: out[bymin][x]=3
        if out[bymax][x]!=6: out[bymax][x]=3
    for y in range(bymin,bymax+1):
        if out[y][bxmin]!=6: out[y][bxmin]=3
        if out[y][bxmax]!=6: out[y][bxmax]=3
    return out