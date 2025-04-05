from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0]) if grid else 0
    blues = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                blues.append((i, j))
    if len(blues) < 2:
        return grid
    blues.sort()
    start = blues[0]
    end = blues[-1]
    cnt = len(blues) - 1
    dr = (end[0] - start[0]) // cnt
    dc = (end[1] - start[1]) // cnt
    for r, c in blues:
        cr, cc = r, c
        while True:
            nr, nc = cr + dr, cc + dc
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                break
            if grid[nr][nc] == 1:
                cr, cc = nr, nc
                continue
            grid[nr][nc] = 2
            cr, cc = nr, nc
    return grid