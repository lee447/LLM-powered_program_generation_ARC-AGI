from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    new = [row[:] for row in grid]
    threes = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==3]
    if not threes:
        return new
    rows = [r for r,_ in threes]
    cols = [c for _,c in threes]
    rmin, rmax = min(rows), max(rows)
    cmin, cmax = min(cols), max(cols)
    sixes = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==6]
    for r,c in sixes:
        if rmin <= r <= rmax:
            if c < cmin:
                cmin = min(cmin, c+1)
            elif c > cmax:
                cmax = max(cmax, c-1)
        if cmin <= c <= cmax:
            if r < rmin:
                rmin = min(rmin, r+1)
            elif r > rmax:
                rmax = max(rmax, r-1)
    for r in range(rmin, rmax+1):
        for c in range(cmin, cmax+1):
            if r in (rmin, rmax) or c in (cmin, cmax):
                if new[r][c]==0:
                    new[r][c]=3
    return new