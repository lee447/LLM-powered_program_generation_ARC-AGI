def solve(grid):
    def extract_columns(grid, start_col, end_col):
        return [row[start_col:end_col] for row in grid]

    def find_non_zero_columns(grid):
        num_cols = len(grid[0])
        for start_col in range(num_cols):
            if any(row[start_col] != 0 for row in grid):
                break
        for end_col in range(num_cols, start_col, -1):
            if any(row[end_col - 1] != 0 for row in grid):
                break
        return start_col, end_col

    start_col, end_col = find_non_zero_columns(grid)
    extracted = extract_columns(grid, start_col, end_col)
    
    def find_non_zero_rows(grid):
        num_rows = len(grid)
        for start_row in range(num_rows):
            if any(cell != 0 for cell in grid[start_row]):
                break
        for end_row in range(num_rows, start_row, -1):
            if any(cell != 0 for cell in grid[end_row - 1]):
                break
        return start_row, end_row

    start_row, end_row = find_non_zero_rows(extracted)
    return extracted[start_row:end_row]