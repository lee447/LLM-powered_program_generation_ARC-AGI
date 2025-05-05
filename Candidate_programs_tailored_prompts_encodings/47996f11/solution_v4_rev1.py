from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    coords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 6]
    rs = [r for r, _ in coords]
    cs = [c for _, c in coords]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    out = [row[:] for row in grid]
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            out[r][c] = 7
    if (c1 - c0) >= (r1 - r0):
        for r in range(r0, r1 + 1):
            out[r][c0] = 1
            out[r][c1] = 1
    else:
        for c in range(c0, c1 + 1):
            out[r0][c] = 1
            out[r1][c] = 1
    return out