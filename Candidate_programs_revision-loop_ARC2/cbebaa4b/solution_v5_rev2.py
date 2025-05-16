from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                color = grid[i][j]
                stack = [(i,j)]
                pts = []
                while stack:
                    y,x = stack.pop()
                    if not (0 <= y < h and 0 <= x < w): continue
                    if seen[y][x] or grid[y][x] != color: continue
                    seen[y][x] = True
                    pts.append((y,x))
                    for dy,dx in dirs:
                        stack.append((y+dy, x+dx))
                ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
                y0, x0 = min(ys), min(xs); y1, x1 = max(ys), max(xs)
                shape = [[0]*(x1-x0+1) for _ in range(y1-y0+1)]
                for yy,xx in pts:
                    shape[yy-y0][xx-x0] = grid[yy][xx]
                comps.append((y0, x0, color, shape))
    order = sorted(comps, key=lambda c: (-c[0], c[1]))
    out = [[0]*w for _ in range(h)]
    y_off = h//5
    for _,__,color,sh in order:
        hh, ww = len(sh), len(sh[0])
        x_off = (w-ww)//2
        for yy in range(hh):
            for xx in range(ww):
                v = sh[yy][xx]
                if v:
                    out[y_off+yy][x_off+xx] = v
        y_off += hh+1
    return out