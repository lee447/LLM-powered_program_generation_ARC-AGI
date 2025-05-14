def solve(grid):
    n, m = len(grid), len(grid[0])
    result = [[0] * m for _ in range(n)]
    for j in range(m):
        non_zero_values = [grid[i][j] for i in range(n) if grid[i][j] != 0]
        for i in range(len(non_zero_values)):
            result[i][j] = non_zero_values[i]
    return result