from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    colors = set()
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v != 0 and v != 3:
                colors.add(v)
    if not colors:
        return out
    shape_color = next(iter(colors))
    rows, cols = set(), set()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == shape_color:
                rows.add(i); cols.add(j)
    sr, sc = sorted(rows), sorted(cols)
    def segments(lst):
        segs, start, prev = [], None, None
        for x in lst:
            if start is None:
                start = prev = x
            elif x == prev + 1:
                prev = x
            else:
                segs.append((start, prev)); start = prev = x
            prev = x
        if start is not None:
            segs.append((start, prev))
        return segs
    row_segs, col_segs = segments(sr), segments(sc)
    if len(row_segs) == 2:
        gap = row_segs[0][1] + 1
        for j in range(w):
            out[gap][j] = 3
    elif len(col_segs) == 2:
        gap = col_segs[0][1] + 1
        for i in range(h):
            out[i][gap] = 3
    return out