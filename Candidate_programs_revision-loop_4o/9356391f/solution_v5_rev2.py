from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_nonzero_row(grid):
        for i, row in enumerate(grid):
            if any(cell != 0 for cell in row):
                return i, row
        return None, None

    def find_nonzero_col(grid):
        for j in range(len(grid[0])):
            if any(grid[i][j] != 0 for i in range(len(grid))):
                return j
        return None

    def fill_pattern(grid, start_row, start_col, pattern):
        for i in range(len(pattern)):
            for j in range(len(pattern[0])):
                grid[start_row + i][start_col + j] = pattern[i][j]

    def extract_pattern(grid, start_row, start_col, size):
        return [row[start_col:start_col + size] for row in grid[start_row:start_row + size]]

    def create_frame(grid, start_row, start_col, size, frame_color):
        for i in range(size):
            grid[start_row][start_col + i] = frame_color
            grid[start_row + size - 1][start_col + i] = frame_color
            grid[start_row + i][start_col] = frame_color
            grid[start_row + i][start_col + size - 1] = frame_color

    first_nonzero_row, first_row = find_nonzero_row(grid)
    first_nonzero_col = find_nonzero_col(grid)

    if first_row is None or first_nonzero_col is None:
        return grid

    pattern_size = 5
    pattern = extract_pattern(grid, first_nonzero_row, first_nonzero_col, pattern_size)

    frame_color = grid[first_nonzero_row][first_nonzero_col + pattern_size]
    create_frame(grid, first_nonzero_row + 6, first_nonzero_col, pattern_size + 2, frame_color)
    fill_pattern(grid, first_nonzero_row + 7, first_nonzero_col + 1, pattern)

    return grid