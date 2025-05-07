from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    new = [row[:] for row in grid]
    threes = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 3]
    if not threes:
        return new
    rows = [r for r, _ in threes]
    cols = [c for _, c in threes]
    rmin0, rmax0, cmin0, cmax0 = min(rows), max(rows), min(cols), max(cols)
    rmin, rmax, cmin, cmax = rmin0, rmax0, cmin0, cmax0
    sixes = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 6]
    for r, c in sixes:
        if rmin0 <= r <= rmax0:
            if c < cmin0:
                cmin = min(cmin, c + 1)
            elif c > cmax0:
                cmax = max(cmax, c - 1)
        if cmin0 <= c <= cmax0:
            if r < rmin0:
                rmin = min(rmin, r + 1)
            elif r > rmax0:
                rmax = max(rmax, r - 1)
    for r in range(rmin, rmax + 1):
        for c in range(cmin, cmax + 1):
            if (r == rmin or r == rmax or c == cmin or c == cmax) and new[r][c] == 0:
                new[r][c] = 3
    return new