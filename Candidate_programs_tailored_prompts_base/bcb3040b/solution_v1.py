from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    points = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    if len(points) != 2:
        return grid
    (r1, c1), (r2, c2) = points
    dr = r2 - r1
    dc = c2 - c1
    steps = max(abs(dr), abs(dc))
    step_r = dr // steps if steps else 0
    step_c = dc // steps if steps else 0
    out = [row[:] for row in grid]
    for i in range(steps + 1):
        r = r1 + i * step_r
        c = c1 + i * step_c
        val = grid[r][c]
        if (r, c) not in points:
            if val == 0:
                out[r][c] = 2
            elif val == 1:
                out[r][c] = 3
    return out