from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    new_rows, new_cols = rows * 2, cols * 2
    result = [[0] * new_cols for _ in range(new_rows)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                for dr in range(2):
                    for dc in range(2):
                        result[r * 2 + dr][c * 2 + dc] = grid[r][c]
    
    return result