def solve(grid):
    rows, cols = len(grid), len(grid[0])
    for c in range(cols):
        non_zero_values = [grid[r][c] for r in range(rows) if grid[r][c] != 0]
        for r in range(rows):
            if non_zero_values:
                grid[r][c] = non_zero_values.pop(0)
            else:
                grid[r][c] = 0
    return grid