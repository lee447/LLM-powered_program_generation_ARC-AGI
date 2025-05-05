from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    hr = [r for r in range(h) if len(set(grid[r])) == 1]
    hc = [c for c in range(w) if len({grid[r][c] for r in range(h)}) == 1]
    hr.sort(), hc.sort()
    r1, r2 = hr[0], hr[1]
    c1, c2 = hc[0], hc[1]
    return [row[c1+1:c2] for row in grid[r1+1:r2]]