def solve(grid):
    R=len(grid);C=len(grid[0])
    out=[row[:] for row in grid]
    for r in range(R-1):
        for c in range(C):
            if grid[r][c]==6 and c>0 and grid[r+1][c-1]==6:
                if c+1<C and out[r][c+1]!=6: out[r][c+1]=4
                if out[r+1][c]!=6: out[r+1][c]=4
            if grid[r][c]==6 and c+1<C and grid[r+1][c+1]==6:
                if c-1>=0 and out[r][c-1]!=6: out[r][c-1]=4
                if out[r+1][c]!=6: out[r+1][c]=4
    return out