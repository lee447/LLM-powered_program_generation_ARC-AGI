def solve(grid):
    h=len(grid); w=len(grid[0])
    bg=grid[0][0]
    axis_col=0
    for c in range(w):
        col= [grid[r][c] for r in range(h)]
        if len(set(col))==1 and col[0]!=bg:
            axis_col=c
            break
    axis_val=grid[0][axis_col]
    out=[row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            v=grid[r][c]
            if v!=bg and v!=axis_val:
                mc=2*axis_col-c
                if 0<=mc<w:
                    out[r][mc]=v
    return out