from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    res = [row[:] for row in grid]
    coords = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 1]
    coords.sort()
    (r0, c0), (r1, c1), (r2, c2) = coords
    dr, dc = r1 - r0, c1 - c0
    if dr > 0:
        last = max(coords, key=lambda x: x[0])
    elif dr < 0:
        last = min(coords, key=lambda x: x[0])
    else:
        if dc > 0:
            last = max(coords, key=lambda x: x[1])
        else:
            last = min(coords, key=lambda x: x[1])
    n, m = len(grid), len(grid[0])
    r, c = last
    while True:
        r += dr
        c += dc
        if 0 <= r < n and 0 <= c < m:
            res[r][c] = 2
        else:
            break
    return res