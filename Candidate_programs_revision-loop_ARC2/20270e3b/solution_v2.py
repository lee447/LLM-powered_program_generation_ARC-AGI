def solve(grid):
    H=len(grid);W=len(grid[0])
    pts=[(i,j) for i in range(H) for j in range(W) if grid[i][j]==1]
    if not pts: return [[4]]
    rs=[i for i,j in pts]; cs=[j for i,j in pts]
    r0=max(0,min(rs)-1); r1=min(H-1,max(rs)+1)
    c0=max(0,min(cs)-1); c1=min(W-1,max(cs)+1)
    out=[]
    for i in range(r0,r1+1):
        row=[]
        for j in range(c0,c1+1):
            row.append(1 if grid[i][j]==1 else 4)
        out.append(row)
    return out