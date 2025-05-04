from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    r1 = r2 = c1 = c2 = None
    for i in range(h - 1):
        for j in range(w - 1):
            if grid[i][j] == 0 and grid[i][j+1] == 0 and grid[i+1][j] == 0 and grid[i+1][j+1] == 0:
                r1, r2, c1, c2 = i, i+1, j, j+1
                break
        if r1 is not None:
            break
    result = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if (i == r1 or i == r2 or j == c1 or j == c2) and grid[i][j] != 2:
                result[i][j] = 0
    return result