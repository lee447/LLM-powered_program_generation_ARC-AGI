from typing import List
import numpy as np

def solve(grid: List[List[int]]) -> List[List[int]]:
    def find_largest_non_zero_area(grid):
        max_area = 0
        best_min_row, best_max_row, best_min_col, best_max_col = 0, 0, 0, 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    min_row, max_row, min_col, max_col = r, r, c, c
                    while max_row + 1 < len(grid) and all(grid[max_row + 1][min_col:max_col + 1]):
                        max_row += 1
                    while max_col + 1 < len(grid[0]) and all(row[max_col + 1] for row in grid[min_row:max_row + 1]):
                        max_col += 1
                    area = (max_row - min_row + 1) * (max_col - min_col + 1)
                    if area > max_area:
                        max_area = area
                        best_min_row, best_max_row, best_min_col, best_max_col = min_row, max_row, min_col, max_col
        return best_min_row, best_max_row, best_min_col, best_max_col

    min_row, max_row, min_col, max_col = find_largest_non_zero_area(grid)
    subgrid = [row[min_col:max_col+1] for row in grid[min_row:max_row+1]]
    return subgrid