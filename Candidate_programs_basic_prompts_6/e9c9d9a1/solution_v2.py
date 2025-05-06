from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    sep_rows = [r for r in range(h) if all(grid[r][c] == 3 for c in range(w))]
    sep_cols = [c for c in range(w) if all(grid[r][c] == 3 for r in range(h))]
    rsegs, csegs = [], []
    prev = -1
    for r in sep_rows:
        rsegs.append((prev+1, r))
        prev = r
    rsegs.append((prev+1, h))
    prev = -1
    for c in sep_cols:
        csegs.append((prev+1, c))
        prev = c
    csegs.append((prev+1, w))
    nr, nc = len(rsegs), len(csegs)
    out = [row[:] for row in grid]
    for i, (rs, re) in enumerate(rsegs):
        for j, (cs, ce) in enumerate(csegs):
            for r in range(rs, re):
                for c in range(cs, ce):
                    if grid[r][c] != 3:
                        if i == 0 and j == 0:
                            out[r][c] = 2
                        elif i == 0 and j == nc-1:
                            out[r][c] = 4
                        elif i == nr-1 and j == 0:
                            out[r][c] = 1
                        elif i == nr-1 and j == nc-1:
                            out[r][c] = 8
                        elif 0 < i < nr-1 and 0 < j < nc-1:
                            out[r][c] = 7
    return out