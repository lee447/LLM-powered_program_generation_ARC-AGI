from typing import List, Tuple
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
                    if seen[y][x] or grid[y][x] not in (color,2): continue
                    seen[y][x] = True
                    pts.append((y,x))
                    for dy,dx in dirs:
                        stack.append((y+dy,x+dx))
                ys = [p[0] for p in pts]
                xs = [p[1] for p in pts]
                y0, y1 = min(ys), max(ys)
                x0, x1 = min(xs), max(xs)
                shape = [[0]*(x1-x0+1) for _ in range(y1-y0+1)]
                for yy,xx in pts:
                    shape[yy-y0][xx-x0] = grid[yy][xx]
                comps.append(((y0,x0),shape))
    # sort by original y0 descending
    comps.sort(key=lambda c: -c[0][0])
    out = [[0]*w for _ in range(h)]
    y_off = h//5
    x_off = (w - max(len(c[1][0]) for c in comps))//2
    for _,sh in comps:
        hh, ww = len(sh), len(sh[0])
        for yy in range(hh):
            for xx in range(ww):
                v = sh[yy][xx]
                if v:
                    out[y_off+yy][x_off+xx] = v
        y_off += hh + 1
    return out