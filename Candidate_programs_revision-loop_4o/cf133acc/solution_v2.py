from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    output = [[0] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                color = grid[r][c]
                if r > 0 and grid[r-1][c] == 0:
                    for rr in range(r, -1, -1):
                        if grid[rr][c] != 0:
                            break
                        output[rr][c] = color
                if c > 0 and grid[r][c-1] == 0:
                    for cc in range(c, -1, -1):
                        if grid[r][cc] != 0:
                            break
                        output[r][cc] = color
                output[r][c] = color
    
    return output