import copy
def solve(grid):
    h=len(grid); w=len(grid[0])
    row_ints=set(); col_ints=set()
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==5 and grid[r][c+1]==5 and grid[r+1][c]==5 and grid[r+1][c+1]==5:
                row_ints.add((r,r+1)); col_ints.add((c,c+1))
    rows=sorted(row_ints); cols=sorted(col_ints)
    interior_rows=[]; boundary_rows=[]
    if rows:
        if rows[0][0]>0:
            boundary_rows.extend(range(0,rows[0][0]))
        for (p0,p1),(n0,n1) in zip(rows,rows[1:]):
            for r in range(p1+1,n0):
                interior_rows.append(r)
        if rows[-1][1]<h-1:
            boundary_rows.extend(range(rows[-1][1]+1,h))
    interior_cols=[]; boundary_cols=[]
    if cols:
        if cols[0][0]>0:
            boundary_cols.extend(range(0,cols[0][0]))
        for (p0,p1),(n0,n1) in zip(cols,cols[1:]):
            for c in range(p1+1,n0):
                interior_cols.append(c)
        if cols[-1][1]<w-1:
            boundary_cols.extend(range(cols[-1][1]+1,w))
    out=copy.deepcopy(grid)
    for r in interior_rows:
        for c in range(w):
            out[r][c]=2
    for c in interior_cols:
        for r in range(h):
            out[r][c]=2
    for r in boundary_rows:
        for c in interior_cols:
            out[r][c]=1
    for c in boundary_cols:
        for r in interior_rows:
            out[r][c]=1
    return out