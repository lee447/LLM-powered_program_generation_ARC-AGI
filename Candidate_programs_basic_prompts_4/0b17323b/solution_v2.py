def solve(grid):
    h=len(grid);w=len(grid[0])
    colors={grid[r][c] for r in range(h) for c in range(w) if grid[r][c]!=0}
    if not colors:
        return [row[:] for row in grid]
    C=colors.pop()
    pts=[(r,c) for r in range(h) for c in range(w) if grid[r][c]==C]
    pts.sort()
    if len(pts)<2:
        return [row[:] for row in grid]
    dr=pts[1][0]-pts[0][0];dc=pts[1][1]-pts[0][1]
    out=[row[:] for row in grid]
    newC=C+1
    r0,c0=pts[0]
    r1,c1=pts[-1]
    r,c=r1,c1
    while True:
        r+=dr; c+=dc
        if 0<=r<h and 0<=c<w:
            if out[r][c]==0:
                out[r][c]=newC
        else:
            break
    r,c=r0,c0
    while True:
        r-=dr; c-=dc
        if 0<=r<h and 0<=c<w:
            if out[r][c]==0:
                out[r][c]=newC
        else:
            break
    return out