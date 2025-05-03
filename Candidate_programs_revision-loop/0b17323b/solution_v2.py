def solve(grid):
    n,len0=len(grid),len(grid[0])
    pts=[(r,c) for r in range(n) for c in range(len0) if grid[r][c]==1]
    if len(pts)<2: return grid
    pts.sort()
    dr=pts[1][0]-pts[0][0]; dc=pts[1][1]-pts[0][1]
    r,c=pts[-1]
    while True:
        r+=dr; c+=dc
        if 0<=r<n and 0<=c<len0:
            grid[r][c]=2
        else:
            break
    return grid