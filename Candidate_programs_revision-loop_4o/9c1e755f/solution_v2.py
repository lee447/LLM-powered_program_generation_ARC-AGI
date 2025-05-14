def solve(grid):
    def fill_horizontal(row, start_col, end_col, value):
        for col in range(start_col, end_col):
            row[col] = value

    def fill_vertical(col, start_row, end_row, value):
        for row in range(start_row, end_row):
            grid[row][col] = value

    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                if r + 1 < rows and grid[r + 1][c] == 0:
                    fill_horizontal(grid[r], c, cols, grid[r][c])
                if c + 1 < cols and grid[r][c + 1] == 0:
                    fill_vertical(c, r, rows, grid[r][c])
    return grid