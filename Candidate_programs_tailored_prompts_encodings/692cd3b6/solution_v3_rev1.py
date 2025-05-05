from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    centers = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    (r1, c1), (r2, c2) = centers
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 4:
                grid[r][c] = 0
    dr = 1 if r2 > r1 else -1
    dc = 1 if c2 > c1 else -1
    for r in range(r1 + dr, r2 + dr, dr):
        if grid[r][c1] == 0:
            grid[r][c1] = 4
    for c in range(c1 + dc, c2 + dc, dc):
        if grid[r2][c] == 0:
            grid[r2][c] = 4
    return grid