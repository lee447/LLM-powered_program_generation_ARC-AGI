from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    r1 = r2 = c1 = c2 = None
    for i in range(h - 1):
        for j in range(w - 1):
            if grid[i][j] == 0 and grid[i][j+1] == 0 and grid[i+1][j] == 0 and grid[i+1][j+1] == 0:
                r1, r2 = i, i+1
                c1, c2 = j, j+1
                break
        if r1 is not None:
            break
    result = [row[:] for row in grid]
    for j in range(w):
        result[r1][j] = 0
        result[r2][j] = 0
    for i in range(h):
        result[i][c1] = 0
        result[i][c2] = 0
    return result