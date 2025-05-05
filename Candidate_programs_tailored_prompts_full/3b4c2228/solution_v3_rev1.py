def solve(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0
    for i in range(n - 1):
        for j in range(m - 1):
            if grid[i][j] == 3 and grid[i][j+1] == 3 and grid[i+1][j] == 3 and grid[i+1][j+1] == 3:
                count += 1
    res = [[0]*3 for _ in range(3)]
    for k in range(min(count, 3)):
        res[k][k] = 1
    return res