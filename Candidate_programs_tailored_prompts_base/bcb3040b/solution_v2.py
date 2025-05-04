def solve(grid):
    h=len(grid);w=len(grid[0])
    pts=[(i,j) for i in range(h) for j in range(w) if grid[i][j]==2]
    (r1,c1),(r2,c2)=pts[0],pts[1]
    dr=0 if r2==r1 else (1 if r2>r1 else -1)
    dc=0 if c2==c1 else (1 if c2>c1 else -1)
    res=[row[:] for row in grid]
    i,j=r1,c1
    while True:
        if res[i][j]==0:res[i][j]=2
        elif res[i][j]==1:res[i][j]=3
        if (i,j)==(r2,c2):break
        i+=dr;j+=dc
    return res