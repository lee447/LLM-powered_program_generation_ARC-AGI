def solve(grid):
    def extract_subgrid(grid, start_row, start_col, height, width):
        return [row[start_col:start_col + width] for row in grid[start_row:start_row + height]]

    def find_non_background_area(grid):
        rows, cols = len(grid), len(grid[0])
        min_row, max_row, min_col, max_col = rows, 0, cols, 0
        background_color = grid[0][0]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != background_color:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        return min_row, max_row + 1, min_col, max_col + 1

    min_row, max_row, min_col, max_col = find_non_background_area(grid)
    subgrid = extract_subgrid(grid, min_row, min_col, max_row - min_row, max_col - min_col)
    
    def rotate_90_clockwise(matrix):
        return [list(reversed(col)) for col in zip(*matrix)]
    
    rotated_subgrid = rotate_90_clockwise(subgrid)
    
    def find_non_background_area_rotated(grid):
        rows, cols = len(grid), len(grid[0])
        min_row, max_row, min_col, max_col = rows, 0, cols, 0
        background_color = grid[0][0]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != background_color:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        return min_row, max_row + 1, min_col, max_col + 1

    min_row, max_row, min_col, max_col = find_non_background_area_rotated(rotated_subgrid)
    final_subgrid = extract_subgrid(rotated_subgrid, min_row, min_col, max_row - min_row, max_col - min_col)
    
    return final_subgrid