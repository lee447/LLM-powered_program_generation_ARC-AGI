from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w - 2):
            if grid[r][c] == 3 and grid[r][c+1] == 3 and grid[r][c+2] == 3:
                out[r][c] = out[r][c+1] = out[r][c+2] = 8
    return out