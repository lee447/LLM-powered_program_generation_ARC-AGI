def solve(grid):
    r=len(grid)
    c=len(grid[0]) if r else 0
    pivot=grid[1][1] if r>1 and c>1 else None
    out=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            v=grid[i][j]
            out[i][j]=v if not (v==pivot and (i,j)!=(1,1)) else 0
    return out