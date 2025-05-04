from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    t = [list(r) for r in zip(*grid)]
    ccw = t[::-1]
    cw = [list(r) for r in zip(*grid[::-1])]
    r180 = [row[::-1] for row in grid[::-1]]
    out = []
    for i in range(n):
        out.append(grid[i] + ccw[i])
    for i in range(n):
        out.append(r180[i] + cw[i])
    return out