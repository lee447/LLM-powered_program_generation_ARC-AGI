from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    reds = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    if len(reds) != 2:
        return grid
    (r1, c1), (r2, c2) = reds
    dr = 0 if r2 == r1 else (1 if r2 > r1 else -1)
    dc = 0 if c2 == c1 else (1 if c2 > c1 else -1)
    length = max(abs(r2 - r1), abs(c2 - c1))
    out = [row[:] for row in grid]
    for k in range(1, length):
        r, c = r1 + k * dr, c1 + k * dc
        if grid[r][c] == 0:
            out[r][c] = 2
        elif grid[r][c] == 1:
            out[r][c] = 3
    return out