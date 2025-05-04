def solve(grid):
    h, w = len(grid), len(grid[0])
    centers = set()
    for i in range(1, h-1):
        for j in range(1, w-1):
            if grid[i][j] == 0 and grid[i-1][j] == 0 and grid[i+1][j] == 0 and grid[i][j-1] == 0 and grid[i][j+1] == 0:
                centers.update([(i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1)])
    result = [row[:] for row in grid]
    for i, j in centers:
        result[i][j] = 3
    return result