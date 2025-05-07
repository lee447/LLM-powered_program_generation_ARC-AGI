def solve(grid):
    H=len(grid);W=len(grid[0])
    N=sum(1 for row in grid for v in row if v!=0)
    m=int(N**0.5)
    br,bc=H//m,W//m
    res=[[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            for r in range(i*br,(i+1)*br):
                for c in range(j*bc,(j+1)*bc):
                    if grid[r][c]!=0:
                        res[i][j]=grid[r][c]
    return res