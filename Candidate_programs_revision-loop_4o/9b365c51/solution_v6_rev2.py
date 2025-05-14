def solve(grid):
    rows, cols = len(grid), len(grid[0])
    output = [[0] * cols for _ in range(rows)]
    for c in range(cols):
        non_zero_values = [grid[r][c] for r in range(rows) if grid[r][c] != 0]
        for r in range(rows):
            if r < len(non_zero_values):
                output[r][c] = non_zero_values[r]
    return output