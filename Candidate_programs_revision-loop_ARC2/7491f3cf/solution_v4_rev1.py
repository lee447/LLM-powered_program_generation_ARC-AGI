from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    stripes = [x for x in range(w) if all(grid[y][x] == border for y in range(h))]
    bw = stripes[1] - stripes[0] - 1
    blocks = [(stripes[i] + 1, stripes[i+1] - 1) for i in range(len(stripes) - 1)]
    shape_x = None
    axis_x = None
    for x0, x1 in blocks:
        coords = {}
        for y in range(1, h-1):
            for x in range(x0, x1+1):
                c = grid[y][x]
                if c != border:
                    coords.setdefault(c, []).append((y, x))
        for c, ps in coords.items():
            if not ps: continue
            ys = [p[0] for p in ps]; xs = [p[1] for p in ps]
            if max(ys) - min(ys) == bw - 1 and max(xs) - min(xs) == bw - 1:
                if len(ps) == bw + 1:
                    shape_x = (c, ps)
                if len(ps) == 2*bw - 1:
                    rel = {(y - min(ys), x - min(xs)) for y, x in ps}
                    plus = {(bw//2, i) for i in range(bw)} | {(i, bw//2) for i in range(bw)}
                    if rel == plus:
                        axis_x = min(xs) + bw//2
    if axis_x is None:
        axis_x = stripes[1] + bw//2
    if shape_x is None:
        return grid
    res = [row[:] for row in grid]
    c, ps = shape_x
    for y, x in ps:
        nx = 2*axis_x - x
        if 0 <= nx < w:
            res[y][nx] = c
    return res