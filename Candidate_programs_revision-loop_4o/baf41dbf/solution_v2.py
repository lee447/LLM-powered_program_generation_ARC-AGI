def solve(grid):
    def fill_horizontal_line(row, start_col, end_col, color):
        for col in range(start_col, end_col + 1):
            grid[row][col] = color

    def fill_vertical_line(col, start_row, end_row, color):
        for row in range(start_row, end_row + 1):
            grid[row][col] = color

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 3:
                if r > 0 and grid[r-1][c] == 3:
                    fill_vertical_line(c, r, r, 3)
                if c > 0 and grid[r][c-1] == 3:
                    fill_horizontal_line(r, c, c, 3)

    return grid