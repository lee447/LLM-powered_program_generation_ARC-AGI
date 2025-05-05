def solve(grid):
    H=len(grid); W=len(grid[0])
    stripe_rows=[i for i in range(H) if len({grid[i][j] for j in range(W)})==1 and grid[i][0]!=0]
    stripe_cols=[j for j in range(W) if len({grid[i][j] for i in range(H)})==1 and grid[0][j]!=0]
    stripe_rows.sort(); stripe_cols.sort()
    sr0,sr1,sr2=stripe_rows; sc0,sc1,sc2=stripe_cols
    ru=range(sr0+1,sr1); rl=range(sr1+1,sr2)
    cu=range(sc0+1,sc1); cl=range(sc1+1,sc2)
    sc=grid[sr0][0]
    TL=[(i,j,grid[i][j]) for i in ru for j in cu if grid[i][j]!=0 and grid[i][j]!=sc]
    TR=[(i,j,grid[i][j]) for i in ru for j in cl if grid[i][j]!=0 and grid[i][j]!=sc]
    out=[row[:] for row in grid]
    dr=sr1-sr0
    for i in rl:
        for j in cu:
            if out[i][j]!=0 and out[i][j]!=sc: out[i][j]=0
    for i in rl:
        for j in cl:
            if out[i][j]!=0 and out[i][j]!=sc: out[i][j]=0
    for i,j,v in TL:
        out[i+dr][j]=v
    for i,j,v in TR:
        out[i+dr][j]=v
    return out