def solve(grid):
    n=len(grid)
    a=grid
    b=[[grid[j][n-1-i] for j in range(n)] for i in range(n)]
    c=[[grid[n-1-i][n-1-j] for j in range(n)] for i in range(n)]
    d=[[grid[n-1-j][i] for j in range(n)] for i in range(n)]
    out=[a[i]+b[i] for i in range(n)]+[c[i]+d[i] for i in range(n)]
    return out