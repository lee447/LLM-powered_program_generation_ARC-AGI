from collections import deque
def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    vis = [[False]*w for _ in range(h)]
    comps_by_color = {}
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c == bg or vis[y][x]:
                continue
            q = deque([(y, x)])
            vis[y][x] = True
            comp = [(y, x)]
            while q:
                cy, cx = q.popleft()
                for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                    ny, nx = cy+dy, cx+dx
                    if 0 <= ny < h and 0 <= nx < w and not vis[ny][nx] and grid[ny][nx]==c:
                        vis[ny][nx] = True
                        q.append((ny, nx))
                        comp.append((ny, nx))
            comps_by_color.setdefault(c, []).append(comp)
    ref = None
    for c, lc in comps_by_color.items():
        if len(lc)==4:
            ref = (c, lc)
            break
    if ref is None:
        return []
    _, refcomps = ref
    boxes = []
    for comp in refcomps:
        ys = [p[0] for p in comp]
        xs = [p[1] for p in comp]
        boxes.append((min(ys), max(ys), min(xs), max(xs)))
    nw = min(boxes, key=lambda b:(b[0],b[2]))
    ne = min(boxes, key=lambda b:(b[0],-b[3]))
    sw = max(boxes, key=lambda b:(b[1],b[2]))
    se = max(boxes, key=lambda b:(b[1],-b[3]))
    NW = (nw[0], nw[2])
    NE = (ne[0], ne[3])
    SW = (sw[1], sw[2])
    H = SW[0] - NW[0] + 1
    W = NE[1] - NW[1] + 1
    vy = NE[0] - NW[0]; vx = NE[1] - NW[1]
    wy = SW[0] - NW[0]; wx = SW[1] - NW[1]
    out = [[bg]*W for _ in range(H)]
    for yo in range(H):
        for xo in range(W):
            alpha = yo/(H-1) if H>1 else 0
            beta = xo/(W-1) if W>1 else 0
            sy = NW[0] + alpha*wy + beta*vy
            sx = NW[1] + alpha*wx + beta*vx
            yy, xx = int(round(sy)), int(round(sx))
            out[yo][xo] = grid[yy][xx]
    return out