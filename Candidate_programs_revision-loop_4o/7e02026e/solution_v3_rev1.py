def solve(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 3:
                if (c > 0 and grid[r][c-1] == 8) or (c < cols-1 and grid[r][c+1] == 8) or (r > 0 and grid[r-1][c] == 8) or (r < rows-1 and grid[r+1][c] == 8):
                    grid[r][c] = 0
    return grid