def solve(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                if c + 1 < cols and grid[r][c + 1] == 2:
                    if r + 1 < rows and grid[r + 1][c] == 2 and grid[r + 1][c + 1] == 2:
                        grid[r][c] = 8
                        grid[r][c + 1] = 8
                        grid[r + 1][c] = 8
                        grid[r + 1][c + 1] = 8
    return grid