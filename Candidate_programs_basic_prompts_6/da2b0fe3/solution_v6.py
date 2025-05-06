from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    minr, maxr, minc, maxc = h, -1, w, -1
    for r in range(h):
        for c in range(w):
            if grid[r][c] != 0:
                if r < minr: minr = r
                if r > maxr: maxr = r
                if c < minc: minc = c
                if c > maxc: maxc = c
    row_cands = []
    dr = maxr - minr
    if dr % 2 == 0:
        row_cands = [(minr + maxr) // 2]
    else:
        m = (minr + maxr) // 2
        row_cands = [m, m + 1]
    col_cands = []
    dc = maxc - minc
    if dc % 2 == 0:
        col_cands = [(minc + maxc) // 2]
    else:
        m = (minc + maxc) // 2
        col_cands = [m, m + 1]
    out = [row[:] for row in grid]
    for r in row_cands:
        if all(grid[r][c] == 0 for c in range(w)):
            for c in range(w):
                out[r][c] = 3
            return out
    for c in col_cands:
        if all(grid[r][c] == 0 for r in range(h)):
            for r in range(h):
                out[r][c] = 3
            return out
    return out