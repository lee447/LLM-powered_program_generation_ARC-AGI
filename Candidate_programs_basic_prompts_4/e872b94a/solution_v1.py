def solve(grid):
    h, w = len(grid), len(grid[0])
    c = 0
    for i in range(h - 1):
        for j in range(w - 1):
            if (grid[i][j] == 5) + (grid[i][j+1] == 5) + (grid[i+1][j] == 5) + (grid[i+1][j+1] == 5) == 3:
                c += 1
    return [[0] for _ in range(c)]