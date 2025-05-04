def solve(grid):
    g = 0
    h, w = len(grid), len(grid[0])
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j] == 3 and grid[i][j+1] == 3 and grid[i+1][j] == 3 and grid[i+1][j+1] == 3:
                g += 1
    return [[1 if i == j and i < g else 0 for j in range(3)] for i in range(3)]