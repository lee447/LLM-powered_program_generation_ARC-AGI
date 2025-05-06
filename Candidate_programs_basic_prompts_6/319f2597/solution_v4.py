def solve(grid):
    n=len(grid); m=len(grid[0])
    c0=c1=None
    for i in range(n-1):
        for j in range(m-1):
            if grid[i][j]==grid[i][j+1]==grid[i+1][j]==grid[i+1][j+1]==0:
                c0, c1 = j, j+1
                break
        if c0 is not None: break
    out=[row[:] for row in grid]
    for i in range(n):
        for j in (c0, c1):
            if out[i][j]!=2: out[i][j]=0
    return out