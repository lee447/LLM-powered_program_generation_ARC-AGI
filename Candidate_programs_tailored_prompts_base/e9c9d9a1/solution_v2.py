from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    nrows, ncols = len(grid), len(grid[0])
    out = [row.copy() for row in grid]
    hdivs = [r for r in range(nrows) if all(grid[r][c] == 3 for c in range(ncols))]
    vdivs = [c for c in range(ncols) if all(grid[r][c] == 3 for r in range(nrows))]
    row_segs, prev = [], 0
    for h in sorted(hdivs):
        if prev <= h - 1:
            row_segs.append((prev, h - 1))
        prev = h + 1
    if prev <= nrows - 1:
        row_segs.append((prev, nrows - 1))
    col_segs, prev = [], 0
    for v in sorted(vdivs):
        if prev <= v - 1:
            col_segs.append((prev, v - 1))
        prev = v + 1
    if prev <= ncols - 1:
        col_segs.append((prev, ncols - 1))
    last_band, last_seg = len(row_segs) - 1, len(col_segs) - 1
    for bi, (r0, r1) in enumerate(row_segs):
        for si, (c0, c1) in enumerate(col_segs):
            color = None
            if bi == 0:
                if si == 0:
                    color = 2
                elif si == last_seg:
                    color = 4
            elif bi == last_band:
                if si == 0:
                    color = 1
                elif si == last_seg:
                    color = 8
            else:
                if 0 < si < last_seg:
                    color = 7
            if color is not None:
                for r in range(r0, r1 + 1):
                    for c in range(c0, c1 + 1):
                        out[r][c] = color
    return out