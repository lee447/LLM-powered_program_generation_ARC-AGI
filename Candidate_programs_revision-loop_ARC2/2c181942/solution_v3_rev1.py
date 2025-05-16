from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = max({c:0 for row in grid for c in row}, key=lambda c: sum(row.count(c) for row in grid))
    seen = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c != bg and not seen[y][x]:
                pts = []
                dq = deque([(y, x)])
                seen[y][x] = True
                while dq:
                    yy, xx = dq.popleft()
                    pts.append((yy, xx))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0 <= ny < h and 0 <= nx < w and not seen[ny][nx] and grid[ny][nx] == c:
                            seen[ny][nx] = True
                            dq.append((ny, nx))
                comps.append((c, pts))
    def avg_x(item):
        pts = item[1]
        return sum(x for y,x in pts)/len(pts)
    comps.sort(key=lambda item:(-len(item[1]), -avg_x(item)))
    comps = comps[:4]
    shapes = []
    for c, pts in comps:
        ys = [y for y, x in pts]
        xs = [x for y, x in pts]
        y0, y1 = min(ys), max(ys)
        x0, x1 = min(xs), max(xs)
        box = [[0]*(x1-x0+1) for _ in range(y1-y0+1)]
        for yy, xx in pts:
            box[yy-y0][xx-x0] = c
        shapes.append((c, box))
    shapes.sort(key=lambda sb: -sum(row.count(sb[0]) for row in sb[1]))
    d_c, d_b = shapes[0]
    l_c, l_b = shapes[1]
    s_c, s_b = shapes[2]
    p_c, p_b = shapes[3]
    dh, dw = len(d_b), len(d_b[0])
    lh, lw = len(l_b), len(l_b[0])
    sh, sw = len(s_b), len(s_b[0])
    ph, pw = len(p_b), len(p_b[0])
    oy = (h - (dh + sh + 1))//2
    ox = (w - (dw + lw + 1))//2
    out = [[bg]*w for _ in range(h)]
    # diamond top-left
    for y in range(dh):
        for x in range(dw):
            if d_b[y][x]:
                out[oy+y][ox+x] = d_c
    # line top-right
    for y in range(lh):
        for x in range(lw):
            if l_b[y][x]:
                out[oy+y][ox+dw+1+x] = l_c
    # square bottom-left
    sy = oy+dh+1
    for y in range(sh):
        for x in range(sw):
            if s_b[y][x]:
                out[sy+y][ox+x] = s_c
    # plus bottom-right
    py = oy+dh+1
    px = ox+dw+1
    for y in range(ph):
        for x in range(pw):
            if p_b[y][x]:
                out[py+y][px+x] = p_c
    return out