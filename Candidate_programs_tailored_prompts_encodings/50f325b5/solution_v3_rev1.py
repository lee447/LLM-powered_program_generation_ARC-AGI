from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    hc = set()
    for i in range(h):
        for j in range(w-2):
            if grid[i][j] == 8 and grid[i][j+1] == 8 and grid[i][j+2] == 8:
                hc.add((i+1, j+1))
    vc = set()
    for i in range(h-2):
        for j in range(w):
            if grid[i][j] == 8 and grid[i+1][j] == 8 and grid[i+2][j] == 8:
                vc.add((i+1, j))
    centers = hc & vc
    res = [row[:] for row in grid]
    for r, c in centers:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                rr, cc = r+dr, c+dc
                if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] in (0, 8):
                    res[rr][cc] = 8
    return res