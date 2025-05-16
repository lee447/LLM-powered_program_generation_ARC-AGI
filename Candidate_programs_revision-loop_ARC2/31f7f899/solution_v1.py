from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = 8
    # find big vertical stripe
    vert = {}
    for x in range(w):
        cnt = sum(1 for y in range(h) if grid[y][x] != bg)
        if cnt > 1:
            vert[x] = cnt
    xv = max(vert, key=vert.get)
    ys = [y for y in range(h) if grid[y][xv] != bg]
    y0, y1 = min(ys), max(ys)
    # find big horizontal stripe
    hor = {}
    for y in range(h):
        cnt = sum(1 for x in range(w) if grid[y][x] != bg)
        if cnt > 1:
            hor[y] = cnt
    yh = max(hor, key=hor.get)
    # collect small vertical stripes (not big cross)
    small = []
    for x in range(w):
        if x == xv: continue
        col = [y for y in range(h) if grid[y][x] != bg]
        if len(col) > 1:
            small.append((x, min(col), max(col), grid[col[0]][x]))
    if not small:
        return [row[:] for row in grid]
    # choose the stripe with smallest range and extend it
    small.sort(key=lambda t: t[2]-t[1])
    x_ext, y_min_ext, y_max_ext, c_ext = small[0]
    # choose the stripe with largest range and shrink it
    x_shr, y_min_shr, y_max_shr, c_shr = small[-1]
    # middle ones stay
    mids = small[1:-1]
    out = [row[:] for row in grid]
    # clear old small stripes
    for x, ym, yM, c in small:
        for y in range(ym, yM+1):
            out[y][x] = bg
    # draw extended stripe to match big vertical
    for y in range(y0, y1+1):
        out[y][x_ext] = c_ext
    # draw shrunk stripe by cropping one at each end
    if y_max_shr - y_min_shr + 1 > 2:
        for y in range(y_min_shr+1, y_max_shr):
            out[y][x_shr] = c_shr
    # draw middles unchanged
    for x, ym, yM, c in mids:
        for y in range(ym, yM+1):
            out[y][x] = c
    return out