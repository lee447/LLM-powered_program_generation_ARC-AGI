from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    min_r, max_r = h, -1
    min_c, max_c = w, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0:
                if r < min_r: min_r = r
                if r > max_r: max_r = r
                if c < min_c: min_c = c
                if c > max_c: max_c = c
    axis_row = (min_r + max_r + 1) // 2
    axis_col = (min_c + max_c + 1) // 2
    out = [row[:] for row in grid]
    if all(grid[axis_row][c] == 0 for c in range(w)):
        for c in range(w):
            out[axis_row][c] = 3
    else:
        for r in range(h):
            out[r][axis_col] = 3
    return out