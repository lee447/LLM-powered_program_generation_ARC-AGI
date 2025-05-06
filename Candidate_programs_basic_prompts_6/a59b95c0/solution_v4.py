def solve(grid):
    h, w = len(grid), len(grid[0])
    k = len({c for row in grid for c in row})
    return [[grid[i % h][j % w] for j in range(w * k)] for i in range(h * k)]