def solve(grid):
    n = len(grid)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j or i + j == n - 1:
                row.append(grid[i][j])
        result.append(row)
    return result