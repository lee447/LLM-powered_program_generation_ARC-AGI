def solve(grid):
    h=len(grid); w=len(grid[0])
    res=[row[:] for row in grid]
    fives=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==5]
    if len(fives)!=2: return res
    (r1,c1),(r2,c2)=fives
    rmin,rmax=min(r1,r2),max(r1,r2)
    cmin,cmax=min(c1,c2),max(c1,c2)
    for r in range(rmin, rmax+1):
        for c in range(cmin, cmax+1):
            if res[r][c]==0:
                res[r][c]=4
    return res