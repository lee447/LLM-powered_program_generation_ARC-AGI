from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    centers = []
    for i in range(1, H-1):
        for j in range(1, W-1):
            if grid[i][j] == 3 and grid[i-1][j] == 3 and grid[i+1][j] == 3 and grid[i][j-1] == 3 and grid[i][j+1] == 3:
                centers.append((i, j))
    n = len(centers)
    for a in range(n):
        r1, c1 = centers[a]
        for b in range(a+1, n):
            r2, c2 = centers[b]
            dr = r2 - r1
            dc = c2 - c1
            if abs(dr) == abs(dc) and dr != 0:
                step_r = 1 if dr > 0 else -1
                step_c = 1 if dc > 0 else -1
                for k in range(1, abs(dr)):
                    rr = r1 + k * step_r
                    cc = c1 + k * step_c
                    if res[rr][cc] == 0:
                        res[rr][cc] = 2
    return res