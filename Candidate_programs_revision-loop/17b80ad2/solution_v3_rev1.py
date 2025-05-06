from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    for c in range(w):
        if grid[h-1][c] == 0:
            continue
        next_color = None
        for r in range(h-1, -1, -1):
            if grid[r][c] != 0:
                next_color = grid[r][c]
            elif next_color is not None:
                res[r][c] = next_color
    return res