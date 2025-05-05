def solve(grid):
    h=len(grid);w=len(grid[0])
    out=[row[:] for row in grid]
    m=min(h,w)
    idxs=[i for i in range(m) if grid[i][i]==1]
    if len(idxs)>=2:
        step=idxs[1]-idxs[0]
        pos=idxs[-1]+step
        while pos<m:
            out[pos][pos]=2
            pos+=step
    return out