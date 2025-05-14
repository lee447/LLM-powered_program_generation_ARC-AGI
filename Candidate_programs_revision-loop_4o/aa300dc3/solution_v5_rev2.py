def solve(grid):
    n = len(grid)
    m = len(grid[0])
    def flood_fill(x, y):
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 8:
            return
        grid[x][y] = 0
        flood_fill(x-1, y)
        flood_fill(x+1, y)
        flood_fill(x, y-1)
        flood_fill(x, y+1)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 8:
                flood_fill(i, j)
                return grid
    return grid