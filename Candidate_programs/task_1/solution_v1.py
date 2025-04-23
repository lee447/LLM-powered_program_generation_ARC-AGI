def solve(grid):
    r=len(grid);c=len(grid[0])if grid else 0
    n=0
    for i in range(r-1):
        for j in range(c-1):
            if grid[i][j]==3 and grid[i][j+1]==3 and grid[i+1][j]==3 and grid[i+1][j+1]==3:
                n+=1
    out=[[0]*3 for _ in range(3)]
    for k in range(min(n,3)):
        out[k][k]=1
    return out