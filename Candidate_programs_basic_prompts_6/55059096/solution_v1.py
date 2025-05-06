from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    centers = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 3:
                if 0 < r < h - 1 and 0 < c < w - 1 and grid[r-1][c] == 3 and grid[r+1][c] == 3 and grid[r][c-1] == 3 and grid[r][c+1] == 3:
                    centers.append((r, c))
    res = [row[:] for row in grid]
    for i in range(len(centers)):
        for j in range(i + 1, len(centers)):
            r1, c1 = centers[i]
            r2, c2 = centers[j]
            dr = r2 - r1
            dc = c2 - c1
            if abs(dr) == abs(dc) and abs(dr) > 1:
                sr = 1 if dr > 0 else -1
                sc = 1 if dc > 0 else -1
                for k in range(1, abs(dr)):
                    rr = r1 + k * sr
                    cc = c1 + k * sc
                    if res[rr][cc] == 0:
                        res[rr][cc] = 2
    return res