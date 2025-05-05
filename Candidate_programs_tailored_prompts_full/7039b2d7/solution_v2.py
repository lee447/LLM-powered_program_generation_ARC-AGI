def solve(grid):
    H=len(grid);W=len(grid[0])
    stripe_rows=[i for i in range(H) if all(grid[i][j]==grid[i][0] for j in range(W))]
    stripe_cols=[j for j in range(W) if all(grid[i][j]==grid[0][j] for i in range(H))]
    stripe_rows.sort();stripe_cols.sort()
    row_intervals=[];prev=-1
    for r in stripe_rows:
        if r-prev>1:row_intervals.append((prev+1,r-1))
        prev=r
    if H-1-prev>0:row_intervals.append((prev+1,H-1))
    col_intervals=[];prev=-1
    for c in stripe_cols:
        if c-prev>1:col_intervals.append((prev+1,c-1))
        prev=c
    if W-1-prev>0:col_intervals.append((prev+1,W-1))
    return [[grid[r0][c0] for (c0,_) in col_intervals] for (r0,_) in row_intervals]