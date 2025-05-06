def solve(grid):
    h=len(grid); w=len(grid[0])
    cnt=0
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j]==3 and grid[i][j+1]==3 and grid[i+1][j]==3 and grid[i+1][j+1]==3:
                cnt+=1
    res=[[0]*3 for _ in range(3)]
    for i in range(min(cnt,3)):
        res[i][i]=1
    return res