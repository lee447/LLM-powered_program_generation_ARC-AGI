def solve(grid):
    h=len(grid);w=len(grid[0])
    out=[row[:] for row in grid]
    starts=[]
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j]==5 and grid[i][j+1]==5 and grid[i+1][j]==5 and grid[i+1][j+1]==5:
                starts.append((i,j))
    rows=sorted({i for i,j in starts})
    cols=sorted({j for i,j in starts})
    stripe_rows=[]
    for k in range(len(rows)-1):
        for r in range(rows[k]+2,rows[k+1]):
            stripe_rows.append(r)
    stripe_cols=[]
    for k in range(len(cols)-1):
        for c in range(cols[k]+2,cols[k+1]):
            stripe_cols.append(c)
    left=list(range(0,cols[0]))
    right=list(range(cols[-1]+2,w))
    top=list(range(0,rows[0]))
    bottom=list(range(rows[-1]+2,h))
    for r in stripe_rows:
        for j in range(w):
            if out[r][j]==0: out[r][j]=2
    for c in stripe_cols:
        for i in range(h):
            if out[i][c]==0: out[i][c]=2
    for r in stripe_rows:
        for j in left+right:
            if out[r][j]==0: out[r][j]=1
    for c in stripe_cols:
        for i in top+bottom:
            if out[i][c]==0: out[i][c]=1
    return out