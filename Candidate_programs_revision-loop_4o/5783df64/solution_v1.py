def solve(grid):
    n = len(grid)
    m = len(grid[0])
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            if grid[i][j] != 0:
                row.append(grid[i][j])
        if row:
            result.append(row)
    return result