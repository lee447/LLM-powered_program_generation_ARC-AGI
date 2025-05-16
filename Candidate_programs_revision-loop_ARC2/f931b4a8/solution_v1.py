def solve(grid):
    n = len(grid)
    h = n // 2
    w = len(grid[0]) // 2
    C = [row[:w] for row in grid[h:]]
    D = [row[w:] for row in grid[h:]]
    return [[C[i][j] if D[i][j] == 0 else D[i][j] for j in range(w)] for i in range(h)]