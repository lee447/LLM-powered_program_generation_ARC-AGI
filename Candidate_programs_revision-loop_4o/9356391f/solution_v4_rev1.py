from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_non_zero_row(grid):
        for i, row in enumerate(grid):
            if any(cell != 0 for cell in row):
                return i, row
        return None, None

    def find_non_zero_col(grid):
        for j in range(len(grid[0])):
            if any(grid[i][j] != 0 for i in range(len(grid))):
                return j
        return None

    def fill_pattern(grid, start_row, start_col, pattern):
        for i in range(len(pattern)):
            for j in range(len(pattern[0])):
                grid[start_row + i][start_col + j] = pattern[i][j]

    def extract_pattern(grid, start_row, start_col, height, width):
        return [row[start_col:start_col + width] for row in grid[start_row:start_row + height]]

    def create_output_grid(grid, pattern, start_row, start_col):
        output_grid = [row[:] for row in grid]
        fill_pattern(output_grid, start_row, start_col, pattern)
        return output_grid

    first_non_zero_row, first_row = find_non_zero_row(grid)
    first_non_zero_col = find_non_zero_col(grid)

    if first_non_zero_row is None or first_non_zero_col is None:
        return grid

    pattern_height = 2
    pattern_width = len(grid[0])

    pattern = extract_pattern(grid, first_non_zero_row, 0, pattern_height, pattern_width)

    output_grid = create_output_grid(grid, pattern, 6, 0)

    return output_grid