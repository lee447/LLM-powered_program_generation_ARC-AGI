from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    def f(x):
        if x == 0: return 8
        if x == 8: return 0
        if x == 6: return 7
        if x == 7: return 6
        return x
    for r in range(h):
        if grid[r][0] == 4 and grid[r][w-1] == 4:
            for c in range(1, w-1):
                out[r][c] = f(grid[r][c])
    for c in range(w):
        if grid[0][c] == 4 and grid[h-1][c] == 4:
            for r in range(1, h-1):
                out[r][c] = f(grid[r][c])
    return out