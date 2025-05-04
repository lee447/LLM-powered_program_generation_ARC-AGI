def solve(grid):
    m=len(grid);n=len(grid[0])
    colors=set(x for row in grid for x in row if x!=0)
    shape=colors.pop() if colors else 0
    cmap={8:2,3:1,5:4}
    fill=cmap.get(shape,1)
    return [[0 if grid[i][j]==shape else fill for j in range(n)] for i in range(m)]