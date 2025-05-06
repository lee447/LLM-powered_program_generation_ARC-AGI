def solve(grid):
    n = len(grid)
    m = len(grid[0])
    k = len({v for row in grid for v in row})
    return [[grid[i % n][j % m] for j in range(m * k)] for i in range(n * k)]