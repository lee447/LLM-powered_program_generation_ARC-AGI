def solve(grid):
    n = len(grid)
    m = len(grid[0])
    color = max(max(row) for row in grid)
    output = [[0] * (n * m) for _ in range(n * m)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == color:
                for x in range(n):
                    for y in range(m):
                        output[i * n + x][j * m + y] = grid[x][y]
    return output