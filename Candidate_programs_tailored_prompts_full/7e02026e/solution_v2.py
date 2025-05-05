def solve(grid):
    h=len(grid); w=len(grid[0])
    pockets=[]
    for i in range(1,h-1):
        for j in range(1,w-1):
            if grid[i][j]==0 and grid[i-1][j]==0 and grid[i+1][j]==0 and grid[i][j-1]==0 and grid[i][j+1]==0:
                pockets.append((i,j))
    pockets.sort(key=lambda rc: rc[0]-rc[1])
    for r,c in pockets[:2]:
        grid[r][c]=3
        grid[r-1][c]=3
        grid[r+1][c]=3
        grid[r][c-1]=3
        grid[r][c+1]=3
    return grid