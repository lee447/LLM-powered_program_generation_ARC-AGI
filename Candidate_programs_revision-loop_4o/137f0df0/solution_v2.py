from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    result = [[0] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 5:
                result[r][c] = 5
            elif grid[r][c] == 0:
                if r % 3 == 2:
                    result[r][c] = 1
                else:
                    result[r][c] = 0
            else:
                result[r][c] = 2
    
    for r in range(0, rows, 3):
        for c in range(cols):
            if grid[r][c] == 0:
                result[r][c] = 2
    
    return result