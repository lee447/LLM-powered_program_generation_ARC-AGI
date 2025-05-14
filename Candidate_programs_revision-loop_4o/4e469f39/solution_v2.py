def solve(grid):
    def find_first_nonzero_row(grid):
        for i, row in enumerate(grid):
            if any(cell != 0 for cell in row):
                return i
        return -1

    def find_first_nonzero_col(grid):
        for j in range(len(grid[0])):
            if any(row[j] != 0 for row in grid):
                return j
        return -1

    def fill_row_with_color(grid, row_idx, color):
        for j in range(len(grid[0])):
            if grid[row_idx][j] == 0:
                grid[row_idx][j] = color

    def fill_col_with_color(grid, col_idx, color):
        for i in range(len(grid)):
            if grid[i][col_idx] == 0:
                grid[i][col_idx] = color

    first_nonzero_row = find_first_nonzero_row(grid)
    first_nonzero_col = find_first_nonzero_col(grid)

    if first_nonzero_row != -1:
        fill_row_with_color(grid, first_nonzero_row - 1, 2)

    if first_nonzero_col != -1:
        fill_col_with_color(grid, first_nonzero_col - 1, 2)

    return grid