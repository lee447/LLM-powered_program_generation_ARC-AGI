def solve(grid):
    h = len(grid)
    w = len(grid[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] in (1,8):
                if j-1>=0 and grid[i][j-1]==0 and grid[i][j+1 if j+1<w else j]==0:
                    out[i][j-1]=4
                    out[i][j+1 if j+1<w else j]=4
    return out