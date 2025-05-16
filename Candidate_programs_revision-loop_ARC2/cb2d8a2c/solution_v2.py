def solve(grid):
    h=len(grid); w=len(grid[0])
    cols=set(grid[r][c] for r in range(h) for c in range(w) if grid[r][c]!=8)
    c=[x for x in cols if sum(grid[r][c2]==x for r in range(h) for c2 in range(w))==1][0]
    res=[row[:] for row in grid]
    for r in range(h):
        for cc in range(w):
            if res[r][cc]==c: sy, sx=r, cc
    pts=[(r,c2) for r in range(h) for c2 in range(w) if grid[r][c2]!=8 and grid[r][c2]!=c]
    ys=[p[0] for p in pts]; xs=[p[1] for p in pts]
    y0,y1=min(ys),max(ys); x0,x1=min(xs),max(xs)
    midy=(y0+y1)//2; midx=(x0+x1)//2
    for y in range(min(sy,midy),max(sy,midy)+1): res[y][sx]=c
    for x in range(min(sx,midx),max(sx,midx)+1): res[midy][x]=c
    return res