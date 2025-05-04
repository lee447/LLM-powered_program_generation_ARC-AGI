from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    greys = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 5]
    (r1, c1), (r2, c2) = sorted(greys)
    rmin, rmax = min(r1, r2), max(r1, r2)
    cmin, cmax = min(c1, c2), max(c1, c2)
    for i in range(rmin + 1, rmax + 1):
        for j in range(cmin, cmax):
            if grid[i][j] == 0:
                grid[i][j] = 4
    return grid