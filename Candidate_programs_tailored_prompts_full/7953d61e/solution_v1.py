def solve(grid):
    n=len(grid)
    m=len(grid[0])
    h=n*2
    w=m*2
    out=[[0]*w for _ in range(h)]
    for i in range(n):
        for j in range(m):
            out[i][j]=grid[i][j]
    for i in range(n):
        for j in range(m):
            out[i][j+m]=grid[j][m-1-i]
    for i in range(n):
        for j in range(m):
            out[i+n][j]=grid[n-1-i][m-1-j]
    for i in range(n):
        for j in range(m):
            out[i+n][j+m]=grid[n-1-j][i]
    return out