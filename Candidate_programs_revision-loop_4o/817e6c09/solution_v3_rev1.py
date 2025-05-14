def solve(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r][c] == 8 and grid[r][c + 1] == 8 and grid[r + 1][c] == 8 and grid[r + 1][c + 1] == 8:
                grid[r][c] = 2
                grid[r][c + 1] = 2
                grid[r + 1][c] = 2
                grid[r + 1][c + 1] = 2
    return grid