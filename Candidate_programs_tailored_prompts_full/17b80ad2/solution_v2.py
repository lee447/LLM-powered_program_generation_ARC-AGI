from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    res = [row[:] for row in grid]
    stripe_cols = [c for c in range(w) if grid[-1][c] != 0]
    for c in stripe_cols:
        pts = [(r, grid[r][c]) for r in range(h) if grid[r][c] != 0]
        pts.sort(key=lambda x: x[0])
        rows = [r for r,_ in pts]
        vals = [v for _,v in pts]
        for r in range(h):
            j = 0
            while j < len(rows) and rows[j] < r:
                j += 1
            if j >= len(rows):
                res[r][c] = vals[-1]
            else:
                res[r][c] = vals[j]
    return res