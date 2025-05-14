def solve(grid):
    rows, cols = len(grid), len(grid[0])
    output = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 or grid[r][c] == 8:
                if (r > 0 and grid[r-1][c] == 1) or (r < rows - 1 and grid[r+1][c] == 1) or (c > 0 and grid[r][c-1] == 1) or (c < cols - 1 and grid[r][c+1] == 1):
                    output[r][c] = grid[r][c]
    return output