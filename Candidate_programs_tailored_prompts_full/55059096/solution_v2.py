from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    centers = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 3:
                if 0 <= r-1 < h and 0 <= r+1 < h and 0 <= c-1 < w and 0 <= c+1 < w:
                    if grid[r-1][c] == 3 and grid[r+1][c] == 3 and grid[r][c-1] == 3 and grid[r][c+1] == 3:
                        centers.append((r, c))
    out = [row[:] for row in grid]
    for i in range(len(centers)):
        r1, c1 = centers[i]
        for j in range(i+1, len(centers)):
            r2, c2 = centers[j]
            dr, dc = r2 - r1, c2 - c1
            if abs(dr) == abs(dc) and dr != 0:
                sr = dr // abs(dr)
                sc = dc // abs(dc)
                for k in range(1, abs(dr)):
                    rr, cc = r1 + sr * k, c1 + sc * k
                    if out[rr][cc] == 0:
                        out[rr][cc] = 2
    return out