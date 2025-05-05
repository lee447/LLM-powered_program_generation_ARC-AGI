from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    endpoints = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 2]
    (r1, c1), (r2, c2) = endpoints
    dr = 0 if r1 == r2 else (1 if r2 > r1 else -1)
    dc = 0 if c1 == c2 else (1 if c2 > c1 else -1)
    result = [row[:] for row in grid]
    r, c = r1, c1
    while True:
        result[r][c] = 3 if grid[r][c] == 1 else 2
        if (r, c) == (r2, c2):
            break
        r += dr
        c += dc
    return result