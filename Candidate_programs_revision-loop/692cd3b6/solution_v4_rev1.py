from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    centers = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    (r1, c1), (r2, c2) = sorted(centers)
    if r1 + 2 <= r2 - 1:
        rmin, rmax = r1 + 2, r2 - 1
    else:
        rmin, rmax = r2 + 2, r1 - 1
    if c1 < c2:
        cleft, cright = c1, c2 - 1
    else:
        cleft, cright = c2, c1 + 2
    for r in range(rmin, rmax + 1):
        for c in range(cleft, cright + 1):
            if grid[r][c] == 0:
                grid[r][c] = 4
    return grid