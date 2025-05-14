def solve(grid):
    min_row, max_row = len(grid), 0
    min_col, max_col = len(grid[0]), 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != 0:
                min_row = min(min_row, r)
                max_row = max(max_row, r)
                min_col = min(min_col, c)
                max_col = max(max_col, c)
    return [row[min_col:max_col+1] for row in grid[min_row:max_row+1] if any(cell != 0 for cell in row[min_col:max_col+1])]