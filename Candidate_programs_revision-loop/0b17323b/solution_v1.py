def solve(grid):
    h=len(grid);w=len(grid[0])if h else 0
    blues=sorted((r,c)for r in range(h)for c in range(w)if grid[r][c]==1)
    if len(blues)<2: return grid
    dr=blues[1][0]-blues[0][0];dc=blues[1][1]-blues[0][1]
    r,c=blues[-1]
    while True:
        r+=dr;c+=dc
        if 0<=r<h and 0<=c<w:
            grid[r][c]=2
        else:
            break
    return grid