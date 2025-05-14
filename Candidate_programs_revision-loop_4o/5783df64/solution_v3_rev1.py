def solve(grid):
    n = len(grid)
    m = len(grid[0])
    result = []
    for j in range(m):
        row = []
        for i in range(n):
            if grid[i][j] != 0:
                row.append(grid[i][j])
        if row:
            result.append(row)
    return result