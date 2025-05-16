from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    def sign(d): return (d>0)-(d<0)
    def draw_line(c, y0, x0, y1, x1):
        dy, dx = y1-y0, x1-x0
        sy, sx = sign(dy), sign(dx)
        steps = max(abs(dy), abs(dx))
        for i in range(steps+1):
            out[y0+sy*i][x0+sx*i] = c

    pts = {}
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c not in (0,3):
                pts.setdefault(c, []).append((y,x))

    for c, ps in pts.items():
        n = len(ps)
        if n < 2:
            continue
        ys = [p[0] for p in ps]
        xs = [p[1] for p in ps]
        y0, y1 = min(ys), max(ys)
        x0, x1 = min(xs), max(xs)
        # if there is at least one horizontal and one vertical pair, draw a rectangle frame
        has_h = any(y1_ == y2 for y1_,x1_ in ps for y2,x2 in ps if y1_ == y2 and x1_!=x2)
        has_v = any(x1_ == x2 for y1_,x1_ in ps for y2,x2 in ps if x1_ == x2 and y1_!=y2)
        if has_h and has_v:
            for x in range(x0, x1+1):
                out[y0][x] = c
                out[y1][x] = c
            for y in range(y0, y1+1):
                out[y][x0] = c
                out[y][x1] = c
        else:
            for i in range(n):
                for j in range(i+1, n):
                    yA, xA = ps[i]
                    yB, xB = ps[j]
                    dy, dx = yB-yA, xB-xA
                    if dy == 0 or dx == 0 or abs(dy) == abs(dx):
                        draw_line(c, yA, xA, yB, xB)
    return out