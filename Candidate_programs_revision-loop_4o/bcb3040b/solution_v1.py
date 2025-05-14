def solve(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                if r + 1 < rows and grid[r + 1][c] == 0:
                    grid[r + 1][c] = 2
                if c + 1 < cols and grid[r][c + 1] == 0:
                    grid[r][c + 1] = 2
                if r + 1 < rows and c + 1 < cols and grid[r + 1][c + 1] == 0:
                    grid[r + 1][c + 1] = 3
    return grid