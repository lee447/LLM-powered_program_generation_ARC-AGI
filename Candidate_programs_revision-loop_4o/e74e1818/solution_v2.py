def solve(grid):
    def find_non_zero_row(grid, start_row):
        for i in range(start_row, len(grid)):
            if any(cell != 0 for cell in grid[i]):
                return i
        return -1

    def find_non_zero_col(grid, start_col):
        for j in range(start_col, len(grid[0])):
            if any(grid[i][j] != 0 for i in range(len(grid))):
                return j
        return -1

    def swap_rows(grid, row1, row2):
        grid[row1], grid[row2] = grid[row2], grid[row1]

    def swap_cols(grid, col1, col2):
        for i in range(len(grid)):
            grid[i][col1], grid[i][col2] = grid[i][col2], grid[i][col1]

    row = 0
    while row < len(grid):
        next_row = find_non_zero_row(grid, row)
        if next_row == -1:
            break
        swap_rows(grid, row, next_row)
        row += 1

    col = 0
    while col < len(grid[0]):
        next_col = find_non_zero_col(grid, col)
        if next_col == -1:
            break
        swap_cols(grid, col, next_col)
        col += 1

    return grid