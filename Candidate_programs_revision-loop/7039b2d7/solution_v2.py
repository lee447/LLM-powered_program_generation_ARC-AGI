def solve(grid):
    nrows=len(grid); ncols=len(grid[0])
    hlines=[i for i in range(nrows) if len(set(grid[i]))==1]
    interior_h=[i for i in hlines if 0<i<nrows-1]
    vlines=[]
    for j in range(ncols):
        col0=grid[0][j]; ok=True
        for i in range(1,nrows):
            if grid[i][j]!=col0:
                ok=False; break
        if ok: vlines.append(j)
    interior_v=[j for j in vlines if 0<j<ncols-1]
    rows=len(interior_h)+1; cols=len(interior_v)+1
    for i in range(nrows):
        if i not in hlines:
            i0=i; break
    for j in range(ncols):
        if j not in vlines:
            j0=j; break
    bg=grid[i0][j0]
    return [[bg]*cols for _ in range(rows)]