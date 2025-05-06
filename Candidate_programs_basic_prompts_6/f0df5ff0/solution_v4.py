def solve(grid):
    h=len(grid)
    w=len(grid[0])
    centers=[(i,j) for i in range(h) for j in range(w) if grid[i][j]==1]
    out=[row[:] for row in grid]
    for r,c in centers:
        for dr in(-1,0,1):
            for dc in(-1,0,1):
                rr,cc=r+dr,c+dc
                if 0<=rr<h and 0<=cc<w and out[rr][cc]==0:
                    out[rr][cc]=1
    return out