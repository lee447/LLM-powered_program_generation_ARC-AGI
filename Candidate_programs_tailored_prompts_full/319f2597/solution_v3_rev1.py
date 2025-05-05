from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    out = [row[:] for row in grid]
    for r in range(h - 1):
        for c in range(w - 1):
            if (grid[r][c] == 0 and grid[r][c+1] == 0 and
                grid[r+1][c] == 0 and grid[r+1][c+1] == 0):
                for rr in range(r + 2):
                    out[rr][c] = 0
                    out[rr][c+1] = 0
    return out