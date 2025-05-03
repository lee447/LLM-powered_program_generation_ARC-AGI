def solve(grid):
    H=len(grid);W=len(grid[0])
    out=[row[:] for row in grid]
    pts=sorted((r,c) for r in range(H) for c in range(W) if grid[r][c]==1)
    if len(pts)<2: return out
    dr=pts[1][0]-pts[0][0]; dc=pts[1][1]-pts[0][1]
    r,c=pts[-1]
    while True:
        r+=dr; c+=dc
        if not (0<=r<H and 0<=c<W): break
        out[r][c]=2
    return out