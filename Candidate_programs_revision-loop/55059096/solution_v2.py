from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    centers = []
    for i in range(1, h-1):
        for j in range(1, w-1):
            if grid[i][j] == 3 and grid[i-1][j] == 3 and grid[i+1][j] == 3 and grid[i][j-1] == 3 and grid[i][j+1] == 3:
                centers.append((i, j))
    def sign(x):
        return (x > 0) - (x < 0)
    for (i1, j1) in centers:
        for (i2, j2) in centers:
            dr = i2 - i1
            dc = j2 - j1
            if abs(dr) == abs(dc) and dr != 0:
                step_r, step_c = sign(dr), sign(dc)
                for k in range(1, abs(dr)):
                    r, c = i1 + k*step_r, j1 + k*step_c
                    if res[r][c] == 0:
                        res[r][c] = 2
    return res