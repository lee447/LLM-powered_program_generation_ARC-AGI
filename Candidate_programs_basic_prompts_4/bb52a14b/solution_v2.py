from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if grid[r][c] in (1, 8):
                for dc in (-1, 1):
                    nc = c + dc
                    if 0 <= nc < w and grid[r][nc] == 0:
                        out[r][nc] = 4
    return out