def solve(grid):
    h=len(grid)
    w=len(grid[0])
    c=next(j for j in range(w) if any(grid[i][j]==5 for i in range(h)))
    left=[row[:c] for row in grid]
    right=[row[c+1:] for row in grid]
    lw=len(left[0])
    left_nz=lambda i,j:left[i][j]!=0
    left_z=lambda i,j:left[i][j]==0
    right_nz=[(i,j) for i in range(h) for j in range(lw) if right[i][j]!=0]
    cond1=all(left_nz(i,j) for i,j in right_nz)
    cond2=all(left_z(i,j) for i,j in right_nz)
    if cond1 or cond2:
        return [[left[i][j] if left[i][j]!=0 else right[i][j] for j in range(lw)] for i in range(h)]
    return [row[:] for row in left]