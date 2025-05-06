from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    res = [row[:] for row in grid]
    centers = []
    for r in range(1, h-1):
        for c in range(1, w-1):
            if grid[r][c] == 3 and grid[r-1][c] == 3 and grid[r+1][c] == 3 and grid[r][c-1] == 3 and grid[r][c+1] == 3:
                centers.append((r, c))
    for i in range(len(centers)):
        r1, c1 = centers[i]
        for j in range(i+1, len(centers)):
            r2, c2 = centers[j]
            dr = r2 - r1
            dc = c2 - c1
            if abs(dr) == abs(dc) and dr != 0:
                sr = 1 if dr > 0 else -1
                sc = 1 if dc > 0 else -1
                for k in range(1, abs(dr)):
                    rr = r1 + k * sr
                    cc = c1 + k * sc
                    res[rr][cc] = 2
    return res