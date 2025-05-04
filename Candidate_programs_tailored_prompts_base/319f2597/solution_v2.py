def solve(grid):
    rows=set()
    cols=set()
    for i,row in enumerate(grid):
        for j,v in enumerate(row):
            if v==0:
                rows.add(i)
                cols.add(j)
    out=[r[:] for r in grid]
    for i in range(len(out)):
        for j in range(len(out[0])):
            if i in rows or j in cols:
                out[i][j]=0
    return out