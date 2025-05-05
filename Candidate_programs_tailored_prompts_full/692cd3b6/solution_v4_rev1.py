from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    greys = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    greys.sort()
    (r1, c1), (r2, c2) = greys
    rtop, rbot = min(r1, r2), max(r1, r2)
    cleft, cright = min(c1, c2), max(c1, c2)
    if rtop - 2 >= 0 and rbot + 2 < h:
        row_start, row_end = rtop + 1, rbot - 1
    else:
        row_start, row_end = max(0, rtop - 2), min(h - 1, rbot - 2)
    if cleft - 2 >= 0 and cright + 2 < w:
        col_start, col_end = cleft, cright - 2
    else:
        col_start, col_end = max(0, cleft - 2), min(w - 1, cright + 2)
    out = [row[:] for row in grid]
    for i in range(row_start, row_end + 1):
        for j in range(col_start, col_end + 1):
            if out[i][j] == 0:
                out[i][j] = 4
    return out