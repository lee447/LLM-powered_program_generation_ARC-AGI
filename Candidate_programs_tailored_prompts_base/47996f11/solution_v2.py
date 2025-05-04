def solve(grid):
    h=len(grid); w=len(grid[0])
    mid=w//2
    stripe_cols=[mid-1,mid]
    out=[row[:] for row in grid]
    stripe_rows=[r for r in range(h) if any(grid[r][c]==6 for c in stripe_cols)]
    for r in stripe_rows:
        for c in stripe_cols:
            if grid[r][c]==6: out[r][c]=7
    if len(stripe_rows)>3:
        for c in (mid-2,mid+1):
            for r in stripe_rows:
                if 0<=r<h and 0<=c<w and grid[r][c]==8:
                    out[r][c]=9
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j]==5 and grid[i][j+1]==5 and grid[i+1][j]==5 and grid[i+1][j+1]==5:
                for di,dj in [(-2,0),(0,-2),(2,0),(0,2)]:
                    ii=i+di; jj=j+dj
                    if 0<=ii<h-1 and 0<=jj<w-1:
                        vals=[grid[ii][jj],grid[ii][jj+1],grid[ii+1][jj],grid[ii+1][jj+1]]
                        if all(v in (1,3) for v in vals):
                            for a in (ii,ii+1):
                                for b in (jj,jj+1):
                                    out[a][b]=3 if grid[a][b]==1 else 1
    return out