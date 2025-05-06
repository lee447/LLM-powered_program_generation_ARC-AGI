from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bar_row = bar_col = None
    for r in range(h - 1):
        for c in range(w - 1):
            if grid[r][c] == 5 and grid[r][c+1] == 5 and grid[r+1][c] == 5:
                bar_row, bar_col = r, c
                break
        if bar_row is not None:
            break
    target = {grid[r][c] for r in range(bar_row) for c in range(bar_col) if grid[r][c] != 0}
    out = [[0]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v == 5 or (r < bar_row and c < bar_col):
                out[r][c] = v
            elif r > bar_row and c > bar_col and v not in target:
                out[r][c] = v
    return out