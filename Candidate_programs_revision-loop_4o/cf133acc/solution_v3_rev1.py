from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    output = [[0] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                color = grid[r][c]
                for i in range(r, -1, -1):
                    if grid[i][c] == 0:
                        output[i][c] = color
                    else:
                        break
                output[r][c] = color
    
    return output