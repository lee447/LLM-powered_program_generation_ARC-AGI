def solve(grid):
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 7:
                return [row[j:j+8] for row in grid[i:i+6]]
    return grid