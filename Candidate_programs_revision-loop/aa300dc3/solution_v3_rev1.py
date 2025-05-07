from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    zeros = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 0]
    rows_by_D1 = {}
    for r, c in zeros:
        D = r - c
        rows_by_D1.setdefault(D, set()).add(r)
    best1_D = max(rows_by_D1, key=lambda D: len(rows_by_D1[D]))
    best1_count = len(rows_by_D1[best1_D])
    rows_by_D2 = {}
    for r, c in zeros:
        D = r + c
        rows_by_D2.setdefault(D, set()).add(r)
    best2_D = max(rows_by_D2, key=lambda D: len(rows_by_D2[D]))
    best2_count = len(rows_by_D2[best2_D])
    out = [row[:] for row in grid]
    if best1_count >= best2_count:
        D = best1_D
        for r, c in zeros:
            if r - c == D:
                out[r][c] = 8
    else:
        D = best2_D
        for r, c in zeros:
            if r + c == D:
                out[r][c] = 8
    return out