from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c != 0 and not visited[y][x]:
                q = deque([(y,x)])
                visited[y][x] = True
                comp = []
                while q:
                    yy, xx = q.popleft()
                    comp.append((yy, xx))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == c:
                            visited[ny][nx] = True
                            q.append((ny, nx))
                comps.append((c, comp))
    axis_c, axis_comp = max(comps, key=lambda ci: len(ci[1]))
    xs = [x for y,x in axis_comp]
    ys = [y for y,x in axis_comp]
    if len(set(xs))==1:
        vertical = True
        axis_x = xs[0]
        min_y, max_y = min(ys), max(ys)
    else:
        vertical = False
        axis_y = ys[0]
        min_x, max_x = min(xs), max(xs)
    out = [[0]*w for _ in range(h)]
    if vertical:
        for yy in range(min_y, max_y+1):
            out[yy][axis_x] = axis_c
    else:
        for xx in range(min_x, max_x+1):
            out[axis_y][xx] = axis_c
    for c, comp in comps:
        if c == axis_c:
            continue
        if len(comp) == 1:
            y0, x0 = comp[0]
            out[y0][x0] = c
            continue
        if vertical:
            sy, sx = min(comp, key=lambda p:(p[0], -p[1]))
        else:
            sy, sx = min(comp, key=lambda p:(p[1], -p[0]))
        best = None
        bd = 10**9
        for yy, xx in (axis_comp):
            d = max(abs(yy-sy), abs(xx-sx))
            if d < bd:
                bd = d
                best = (yy, xx)
        ty, tx = best
        steps = max(abs(ty-sy), abs(tx-sx))
        for i in range(steps+1):
            yy = sy + (ty-sy)*i//steps if steps else sy
            xx = sx + (tx-sx)*i//steps if steps else sx
            if 0 <= yy < h and 0 <= xx < w and out[yy][xx] != axis_c:
                out[yy][xx] = c
    return out