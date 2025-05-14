def solve(grid):
    rows, cols = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 5:
                if r > 0 and grid[r-1][c] == 2:
                    result[r+1][c] = 4
                if c > 0 and grid[r][c-1] == 2:
                    result[r][c+1] = 4
                if r < rows - 1 and grid[r+1][c] == 2:
                    result[r-1][c] = 4
                if c < cols - 1 and grid[r][c+1] == 2:
                    result[r][c-1] = 4
    for r in range(rows):
        for c in range(cols):
            if result[r][c] == 0:
                if (r > 0 and result[r-1][c] == 4) or (c > 0 and result[r][c-1] == 4) or (r < rows - 1 and result[r+1][c] == 4) or (c < cols - 1 and result[r][c+1] == 4):
                    result[r][c] = 4
    return result