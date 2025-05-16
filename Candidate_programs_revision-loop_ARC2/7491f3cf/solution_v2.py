from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    coords = {}
    for y in range(1, h-1):
        for x in range(1, w-1):
            c = grid[y][x]
            coords.setdefault(c, []).append((y, x))
    def bbox(ps: List[Tuple[int,int]]):
        ys = [p[0] for p in ps]; xs = [p[1] for p in ps]
        return min(ys), max(ys), min(xs), max(xs)
    shape_x = None
    axis_x = None
    for c, ps in coords.items():
        if len(ps) != 9: continue
        y0, y1, x0, x1 = bbox(ps)
        if y1-y0 == 4 and x1-x0 == 4:
            rel = {(y-y0, x-x0) for y,x in ps}
            if all((i, i) in rel or (i, 4-i) in rel for i in range(5)):
                shape_x = (c, ps, (y0, y1, x0, x1))
            plus = {(2, i) for i in range(5)} | {(i, 2) for i in range(5)}
            if rel == plus:
                axis_x = x0 + 2
    if axis_x is None:
        stripes = [x for x in range(w) if all(grid[y][x] == border for y in range(h))]
        stripes = [x for x in stripes if 0 < x < w-1]
        _, _, _, x1 = shape_x[2]
        cand = [x for x in stripes if x > x1]
        axis_x = min(cand) if cand else None
    res = [row[:] for row in grid]
    c, ps, _ = shape_x
    for y, x in ps:
        nx = 2*axis_x - x
        if 0 <= nx < w:
            res[y][nx] = c
    return res