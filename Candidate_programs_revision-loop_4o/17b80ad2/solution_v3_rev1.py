from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    result = [[0] * cols for _ in range(rows)]
    
    for col in range(cols):
        last_non_zero = 0
        for row in range(rows):
            if grid[row][col] != 0:
                last_non_zero = grid[row][col]
            if last_non_zero != 0:
                result[row][col] = last_non_zero
    
    for col in range(cols):
        for row in range(rows - 1, 0, -1):
            if result[row][col] == 0 and result[row - 1][col] != 0:
                result[row][col] = result[row - 1][col] - 1
    
    return result