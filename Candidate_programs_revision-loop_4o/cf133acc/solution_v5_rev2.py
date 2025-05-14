from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    output = [[0] * cols for _ in range(rows)]
    
    for c in range(cols):
        last_color = 0
        for r in range(rows):
            if grid[r][c] != 0:
                last_color = grid[r][c]
            if last_color != 0:
                output[r][c] = last_color
    
    return output