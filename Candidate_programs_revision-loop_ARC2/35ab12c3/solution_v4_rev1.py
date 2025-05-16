from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    dirs = [(-1,-1),(-1,1),(1,-1),(1,1)]
    def sign(x): return 0 if x==0 else (1 if x>0 else -1)
    def connect(c, y0, x0, y1, x1):
        dy, dx = y1-y0, x1-x0
        sy, sx = sign(dy), sign(dx)
        length = max(abs(dy), abs(dx))
        for i in range(length+1):
            out[y0+sy*i][x0+sx*i] = c
    colors = {}
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c not in (0,3):
                colors.setdefault(c, []).append((y,x))
    for c, pts in colors.items():
        n = len(pts)
        ys = [p[0] for p in pts]
        xs = [p[1] for p in pts]
        y0, y1 = min(ys), max(ys)
        x0, x1 = min(xs), max(xs)
        if n == 2:
            (yA,xA),(yB,xB) = pts
            if yA == yB:
                for x in range(min(xA,xB), max(xA,xB)+1): out[yA][x] = c
            elif xA == xB:
                for y in range(min(yA,yB), max(yA,yB)+1): out[y][xA] = c
            elif abs(yB-yA) == abs(xB-xA):
                connect(c, yA, xA, yB, xB)
        elif n > 2:
            # rectangle border
            for x in range(x0, x1+1):
                out[y0][x] = c
                out[y1][x] = c
            for y in range(y0, y1+1):
                out[y][x0] = c
                out[y][x1] = c
        # leave singletons unchanged
    return out