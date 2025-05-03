from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    res = [row[:] for row in grid]
    for j in range(w):
        pts = [(i, grid[i][j]) for i in range(h) if grid[i][j] != 0]
        if not pts:
            continue
        pts.sort()
        prev = -1
        for i, v in pts:
            for r in range(prev + 1, i + 1):
                res[r][j] = v
            prev = i
    return res