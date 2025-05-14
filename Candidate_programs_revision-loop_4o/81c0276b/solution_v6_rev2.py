def solve(grid):
    result = []
    for i in range(1, len(grid), 5):
        row = []
        for j in range(1, len(grid[i]), 5):
            if grid[i][j] != 0:
                row.append(grid[i][j])
            else:
                row.append(grid[i+1][j])
        result.append(row)
    return result