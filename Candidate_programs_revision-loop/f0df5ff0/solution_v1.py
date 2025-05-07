from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if orig[r][c] == 1:
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < h and 0 <= nc < w and orig[nr][nc] == 0:
                            out[nr][nc] = 1
    return out