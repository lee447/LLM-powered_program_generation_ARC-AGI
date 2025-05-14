from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def extract_subgrid(grid, start_row, start_col, height, width):
        return [row[start_col:start_col + width] for row in grid[start_row:start_row + height]]

    def find_largest_non_zero_block(grid):
        max_area = 0
        best_subgrid = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    height = 0
                    while r + height < len(grid) and grid[r + height][c] != 0:
                        height += 1
                    width = 0
                    while c + width < len(grid[0]) and grid[r][c + width] != 0:
                        width += 1
                    area = height * width
                    if area > max_area:
                        max_area = area
                        best_subgrid = extract_subgrid(grid, r, c, height, width)
        return best_subgrid

    return find_largest_non_zero_block(grid)