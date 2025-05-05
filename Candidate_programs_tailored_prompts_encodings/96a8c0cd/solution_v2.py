def solve(grid):
    H=len(grid); W=len(grid[0])
    vertical_centers=[]
    horizontal_centers=[]
    for r in range(H):
        for c in range(W):
            v=grid[r][c]
            if v!=0:
                if r-1>=0 and r+1<H and grid[r-1][c]==v and grid[r+1][c]==v:
                    vertical_centers.append((r,c))
                if c-1>=0 and c+1<W and grid[r][c-1]==v and grid[r][c+1]==v:
                    horizontal_centers.append((r,c))
    out=[row[:] for row in grid]
    cols_global=sorted({c for (_,c) in vertical_centers})
    rows_global=sorted({r for (r,_) in horizontal_centers})
    max_col=cols_global[-1] if cols_global else -1
    max_row=rows_global[-1] if rows_global else -1
    rows_v=sorted({r for (r,_) in vertical_centers})
    for r in rows_v:
        cluster_cols=[c for (rr,c) in vertical_centers if rr==r]
        skip={c+1 for c in cluster_cols}
        for c in range(0, max_col):
            if out[r][c]==0 and c not in skip:
                out[r][c]=2
    cols_h=sorted({c for (_,c) in horizontal_centers})
    for c in cols_h:
        cluster_rows=[r for (r,cc) in horizontal_centers if cc==c]
        skip={r+1 for r in cluster_rows}
        for r in range(0, max_row):
            if out[r][c]==0 and r not in skip:
                out[r][c]=2
    return out