def solve(grid):
    n=len(grid)
    c=0
    for row in grid:
        for v in row:
            if v!=0:
                c=v
                break
        if c!=0:
            break
    mask=[[1 if grid[i][j]==0 else 0 for j in range(n)] for i in range(n)]
    out=[[0]*(n*n) for _ in range(n*n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j]==0:
                for u in range(n):
                    for v in range(n):
                        if mask[u][v]:
                            out[i*n+u][j*n+v]=c
    return out