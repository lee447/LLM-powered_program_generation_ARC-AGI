from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    Y = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 4]
    R = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    if not Y or not R:
        return [row[:] for row in grid]
    Y.sort()
    R.sort()
    y0r, y0c = Y[0]
    offsets = [(r - y0r, c - y0c) for r, c in R]
    out = [row[:] for row in grid]
    for yr, yc in Y:
        for dr, dc in offsets:
            rr, cc = yr + dr, yc + dc
            if 0 <= rr < h and 0 <= cc < w and out[rr][cc] == 0:
                out[rr][cc] = 2
    return out