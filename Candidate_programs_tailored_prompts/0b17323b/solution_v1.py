def solve(grid):
    h=len(grid)
    w=len(grid[0])
    out=[row[:] for row in grid]
    anchors=[(i,j) for i in range(h) for j in range(w) if grid[i][j]==1]
    anchors.sort()
    if len(anchors)<2:
        return out
    dr=anchors[1][0]-anchors[0][0]
    dc=anchors[1][1]-anchors[0][1]
    r,c=anchors[-1]
    while True:
        r+=dr
        c+=dc
        if 0<=r<h and 0<=c<w:
            out[r][c]=2
        else:
            break
    return out