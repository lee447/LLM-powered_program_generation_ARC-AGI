from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    greys = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    greys.sort()
    (r1, c1), (r2, c2) = greys
    # determine which is left/right by column
    if c1 < c2:
        cleft, cright = c1, c2
    else:
        cleft, cright = c2, c1
    # determine which is upper/lower by row
    if r1 < r2:
        rtop, rbot = r1, r2
    else:
        rtop, rbot = r2, r1
    # compute inner edges
    row_start = rtop + 2
    row_end = rbot - 2
    col_start = cleft + 2
    col_end = cright - 2
    # fill
    out = [row[:] for row in grid]
    for i in range(row_start, row_end + 1):
        for j in range(col_start, col_end + 1):
            if out[i][j] == 0:
                out[i][j] = 4
    return out