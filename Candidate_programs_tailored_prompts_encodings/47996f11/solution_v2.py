def solve(grid):
    h=len(grid);w=len(grid[0])
    coords=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==6]
    rs=[r for r,c in coords]; cs=[c for r,c in coords]
    r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
    nr0,nr1=max(0,r0-1),min(h-1,r1+1)
    nc0,nc1=max(0,minc-1),min(w-1,maxc+1)
    hor = (maxc-minc)>=(r1-r0)
    out=[row[:] for row in grid]
    for r in range(nr0,nr1+1):
        for c in range(nc0,nc1+1):
            out[r][c]=7
    if hor:
        for r in range(nr0,nr1+1):
            out[r][nc0]=1; out[r][nc1]=1
    else:
        for c in range(nc0,nc1+1):
            out[nr0][c]=1; out[nr1][c]=1
    return out