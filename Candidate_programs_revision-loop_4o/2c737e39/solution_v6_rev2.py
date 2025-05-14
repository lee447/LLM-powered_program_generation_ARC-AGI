def solve(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                if (r == 0 or grid[r-1][c] == 0) and (c == 0 or grid[r][c-1] == 0):
                    new_grid[r][c] = grid[r][c]
                elif (r > 0 and grid[r-1][c] == grid[r][c]) or (c > 0 and grid[r][c-1] == grid[r][c]):
                    new_grid[r][c] = grid[r][c]
    return new_grid