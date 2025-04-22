from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    vals = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0]
    if not vals:
        return [row[:] for row in grid]
    rs = [r for r, _, _ in vals]
    rmin = min(rs)
    shifts = [0, -1, 0, 1]
    out = [[0]*w for _ in range(h)]
    for r, c, v in vals:
        s = shifts[(r - rmin) % 4]
        out[r][c + s] = v
    return out