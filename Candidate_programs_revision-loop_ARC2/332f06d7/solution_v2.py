def solve(grid):
    h, w = len(grid), len(grid[0])
    new = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0:
                new[i][j] = 1
            elif grid[i][j] == 2:
                new[i][j] = 0
    return new