def solve(grid):
    h = len(grid)
    w = len(grid[0])
    sep_rows = [i for i,row in enumerate(grid) if all(x==4 for x in row)]
    sep_cols = [j for j in range(w) if all(grid[i][j]==4 for i in range(h))]
    row_blocks = []
    prev = -1
    for r in sep_rows+[h]:
        if prev+1<r:
            row_blocks.append((prev+1,r))
        prev = r
    col_blocks = []
    prev = -1
    for c in sep_cols+[w]:
        if prev+1<c:
            col_blocks.append((prev+1,c))
        prev = c
    color = None
    for row in grid:
        for v in row:
            if v not in (0,1,4):
                color = v
    if color is None:
        color = 3
    out = [r[:] for r in grid]
    for br,(r0,r1) in enumerate(row_blocks):
        for bc,(c0,c1) in enumerate(col_blocks):
            ones = [(i-r0,j-c0) for i in range(r0,r1) for j in range(c0,c1) if grid[i][j]==1]
            if any(grid[i][j]==color for i in range(r0,r1) for j in range(c0,c1)):
                for i,j in ones:
                    if (i,j) in ((0,0),(0,c1-c0-1),( (r1-r0-1)//2,(c1-c0-1)//2 )):
                        out[r0+i][c0+j] = color
    return out