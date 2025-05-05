from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    pockets = []
    for r in range(1, h-1):
        for c in range(1, w-1):
            if (g[r][c] == 0 and g[r-1][c] == 0 and g[r+1][c] == 0 and
                g[r][c-1] == 0 and g[r][c+1] == 0):
                pockets.append((r, c))
    pockets.sort(key=lambda x: x[0] - x[1])
    for r, c in pockets[:2]:
        g[r][c] = 3
        g[r-1][c] = 3
        g[r+1][c] = 3
        g[r][c-1] = 3
        g[r][c+1] = 3
    return g