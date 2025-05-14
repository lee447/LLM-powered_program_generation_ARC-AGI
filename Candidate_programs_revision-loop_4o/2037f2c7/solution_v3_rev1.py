from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    def extract_non_zero_area(grid):
        min_row, max_row = len(grid), 0
        min_col, max_col = len(grid[0]), 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)
        return min_row, max_row, min_col, max_col

    min_row, max_row, min_col, max_col = extract_non_zero_area(grid)
    extracted = [row[min_col:max_col+1] for row in grid[min_row:max_row+1]]
    
    for r in range(len(extracted)):
        for c in range(len(extracted[0])):
            if extracted[r][c] != 0:
                extracted[r][c] = 8

    return extracted