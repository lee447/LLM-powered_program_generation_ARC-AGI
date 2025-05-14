def solve(grid):
    n = len(grid)
    m = len(grid[0])
    output = [[0] * (n * m) for _ in range(n * m)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                for x in range(n):
                    for y in range(m):
                        output[x * n + i][y * m + j] = grid[x][y]
    return output