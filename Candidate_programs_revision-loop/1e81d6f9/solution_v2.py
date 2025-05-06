def solve(grid):
    h=len(grid); w=len(grid[0])
    stripe_coords=[(i,j) for i in range(h) for j in range(w) if grid[i][j]==5]
    el=max(i for i,j in stripe_coords)
    ec=max(j for i,j in stripe_coords)
    target=None
    for i in range(el):
        for j in range(ec):
            v=grid[i][j]
            if v and v!=5:
                target=v
                break
        if target is not None:
            break
    out=[row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if out[i][j]==target and not (i<el and j<ec):
                out[i][j]=0
    return out