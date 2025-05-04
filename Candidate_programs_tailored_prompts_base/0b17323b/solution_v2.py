def solve(grid):
    h=len(grid)
    w=len(grid[0])
    blues=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1:
                blues.append((i,j))
    blues.sort()
    if len(blues)<2:
        return [row[:] for row in grid]
    dr=blues[1][0]-blues[0][0]
    dc=blues[1][1]-blues[0][1]
    out=[row[:] for row in grid]
    r,c=blues[-1]
    while True:
        r+=dr
        c+=dc
        if 0<=r<h and 0<=c<w:
            out[r][c]=2
        else:
            break
    return out