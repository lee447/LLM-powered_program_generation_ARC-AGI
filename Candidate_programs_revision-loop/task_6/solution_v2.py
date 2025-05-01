from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    grey_rows = {r for r in range(h) for c in range(w) if grid[r][c] == 5}
    grey_cols = {c for r in range(h) for c in range(w) if grid[r][c] == 5}
    min_r, max_r = min(grey_rows), max(grey_rows)
    min_c, max_c = min(grey_cols), max(grey_cols)
    gap_rows = [r for r in range(min_r, max_r+1) if all(grid[r][c] != 5 for c in range(w))]
    gap_cols = [c for c in range(min_c, max_c+1) if all(grid[r][c] != 5 for r in range(h))]
    for r in gap_rows:
        for c in range(min_c, max_c+1):
            if out[r][c] == 0:
                out[r][c] = 2
    for c in gap_cols:
        for r in range(min_r, max_r+1):
            if out[r][c] == 0:
                out[r][c] = 2
    for r in gap_rows:
        for c in range(0, min_c):
            if out[r][c] == 0:
                out[r][c] = 1
        for c in range(max_c+1, w):
            if out[r][c] == 0:
                out[r][c] = 1
    for c in gap_cols:
        for r in range(0, min_r):
            if out[r][c] == 0:
                out[r][c] = 1
        for r in range(max_r+1, h):
            if out[r][c] == 0:
                out[r][c] = 1
    return out