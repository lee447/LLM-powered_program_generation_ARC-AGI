def solve(grid):
    def fill_horizontal_line(row, start_col, end_col, color):
        for col in range(start_col, end_col + 1):
            grid[row][col] = color

    def fill_vertical_line(col, start_row, end_row, color):
        for row in range(start_row, end_row + 1):
            grid[row][col] = color

    def find_bounds():
        min_row, max_row = len(grid), -1
        min_col, max_col = len(grid[0]), -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 3:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        return min_row, max_row, min_col, max_col

    min_row, max_row, min_col, max_col = find_bounds()

    for r in range(min_row, max_row + 1):
        fill_horizontal_line(r, min_col, max_col, 3)

    for c in range(min_col, max_col + 1):
        fill_vertical_line(c, min_row, max_row, 3)

    return grid