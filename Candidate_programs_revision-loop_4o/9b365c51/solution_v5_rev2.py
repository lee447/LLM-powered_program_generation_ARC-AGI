from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    output = [[0] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                color = grid[r][c]
                for rr in range(r, rows):
                    if grid[rr][c] == 0:
                        break
                    for cc in range(c, cols):
                        if grid[rr][cc] == 0:
                            break
                        output[rr][cc] = color
                break
    
    return output