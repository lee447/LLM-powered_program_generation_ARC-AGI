from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    threes = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 3]
    if not threes:
        return [row[:] for row in grid]
    rows = [r for r, _ in threes]
    cols = [c for _, c in threes]
    rmin0, rmax0, cmin0, cmax0 = min(rows), max(rows), min(cols), max(cols)
    rmin, rmax, cmin, cmax = rmin0, rmax0, cmin0, cmax0
    sixes = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 6]
    for r, c in sixes:
        if rmin0 <= r <= rmax0:
            if c < cmin0:
                cmin = min(cmin, c + 1)
            if c > cmax0:
                cmax = max(cmax, c - 1)
        if cmin0 <= c <= cmax0:
            if r < rmin0:
                rmin = min(rmin, r + 1)
            if r > rmax0:
                rmax = max(rmax, r - 1)
    res = [row[:] for row in grid]
    for r in range(rmin, rmax + 1):
        for c in range(cmin, cmax + 1):
            if (r == rmin or r == rmax or c == cmin or c == cmax):
                if res[r][c] != 6:
                    res[r][c] = 3
            else:
                res[r][c] = 0
    return res