def solve(grid):
    h=len(grid);w=len(grid[0])
    nz=set(v for row in grid for v in row if v!=0)
    k=len(nz)
    pr=None
    for row in grid:
        if row.count(0)==0 and len({v for v in row if v!=0})>1:
            pr=row
            break
    pattern=pr[:k]
    out=[row[:] for row in grid]
    for i,row in enumerate(grid):
        vals={v for v in row if v!=0}
        uniform = vals.pop() if len(vals)==1 else None
        for j,v in enumerate(row):
            if v==0:
                if uniform is None:
                    out[i][j]=pattern[j%k]
                else:
                    out[i][j]=uniform
    return out