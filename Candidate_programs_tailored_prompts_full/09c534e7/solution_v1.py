def solve(grid):
    R=len(grid); C=len(grid[0])
    out=[row[:] for row in grid]
    for i in range(R-4):
        for j in range(C-4):
            b=grid[i][j]
            if b==0: continue
            ok=True
            for k in range(5):
                if grid[i][j+k]!=b or grid[i+4][j+k]!=b or grid[i+k][j]!=b or grid[i+k][j+4]!=b:
                    ok=False; break
            if not ok: continue
            a=grid[i+2][j+2]
            for ii in range(i+1,i+4):
                for jj in range(j+1,j+4):
                    out[ii][jj]=a
    return out