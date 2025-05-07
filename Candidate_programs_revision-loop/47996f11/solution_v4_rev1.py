from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    minr, minc, maxr, maxc = h, w, -1, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 6:
                if r < minr: minr = r
                if r > maxr: maxr = r
                if c < minc: minc = c
                if c > maxc: maxc = c
    res = [row[:] for row in grid]
    for r in range(minr, maxr+1):
        for c in range(minc, maxc+1):
            if grid[r][c] == 6:
                if c-minc < maxc-c:
                    rr = r+1 if r+1 < h else r
                    cc = c-1 if c-1 >= 0 else c
                    res[r][c] = grid[rr][cc]
                else:
                    rc = c+1
                    while rc < w and grid[r][rc] == 6:
                        rc += 1
                    res[r][c] = grid[r][rc] if rc < w else grid[r][c]
    return res