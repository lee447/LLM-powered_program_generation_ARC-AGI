from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0]) if H else 0
    out = [row.copy() for row in grid]
    for c in range(W):
        pts = [(r, grid[r][c]) for r in range(H) if grid[r][c] != 0]
        if len(pts) < 2:
            continue
        pts.sort()
        prev = -1
        for r, col in pts:
            for i in range(prev + 1, r + 1):
                out[i][c] = col
            prev = r
    return out