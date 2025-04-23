def solve(grid):
    h=len(grid);w=len(grid[0])
    out=[row[:] for row in grid]
    for r in range(h):
        row=grid[r]
        run_idxs=[c for c,v in enumerate(row) if v==6]
        if not run_idxs: continue
        i,j=run_idxs[0],run_idxs[-1]
        n=j-i+1
        m=2*n-1
        left_val=row[i-1]
        right_val=row[j+1]
        for k in range(m):
            out[r][i+k]=left_val if k<n else right_val
    return out