def solve(grid):
    def extract_subgrid(grid, start_row, start_col, height, width):
        return [row[start_col:start_col + width] for row in grid[start_row:start_row + height]]

    def find_non_background_area(grid):
        rows, cols = len(grid), len(grid[0])
        min_row, max_row, min_col, max_col = rows, 0, cols, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != grid[0][0]:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        return min_row, max_row + 1, min_col, max_col + 1

    min_row, max_row, min_col, max_col = find_non_background_area(grid)
    return extract_subgrid(grid, min_row, min_col, max_row - min_row, max_col - min_col)