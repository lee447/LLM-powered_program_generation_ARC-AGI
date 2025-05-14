def solve(grid):
    n = len(grid)
    result = [[], [], []]
    for i in range(n // 2 + 1):
        result[0].append(grid[i][i])
        result[1].append(grid[i][n - 1 - i])
        result[2].append(grid[n - 1 - i][i])
    return result