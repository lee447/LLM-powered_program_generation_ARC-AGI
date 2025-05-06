def solve(grid):
    h=len(grid);w=len(grid[0])
    res=[row[:] for row in grid]
    centers=[(i,j)for i in range(h)for j in range(w)if grid[i][j]==1]
    for i,j in centers:
        for di in(-1,0,1):
            for dj in(-1,0,1):
                ni, nj = i+di, j+dj
                if 0<=ni<h and 0<=nj<w and res[ni][nj]==0:
                    res[ni][nj]=1
    return res