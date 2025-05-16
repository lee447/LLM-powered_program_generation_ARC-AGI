import collections
def solve(grid):
    h, w = len(grid), len(grid[0])
    freq = collections.Counter(c for row in grid for c in row)
    bg = max(freq, key=lambda c: freq[c])
    seen = [[False]*w for _ in range(h)]
    comps = []
    from collections import deque
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c != bg and not seen[y][x]:
                dq = deque([(y, x)])
                seen[y][x] = True
                pts = []
                while dq:
                    yy, xx = dq.popleft()
                    pts.append((yy, xx))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0 <= ny < h and 0 <= nx < w and not seen[ny][nx] and grid[ny][nx] == c:
                            seen[ny][nx] = True
                            dq.append((ny, nx))
                comps.append((c, pts))
    shapes = {}
    for c, pts in comps:
        ys = [y for y, x in pts]
        xs = [x for y, x in pts]
        y0, y1 = min(ys), max(ys)
        x0, x1 = min(xs), max(xs)
        bh, bw = y1 - y0 + 1, x1 - x0 + 1
        count = len(pts)
        if bh == 1 or bw == 1:
            t = 'line'
        elif count == bh * bw:
            t = 'square'
        elif count == bh + bw - 1:
            t = 'plus'
        else:
            t = 'diamond'
        box = [[0]*bw for _ in range(bh)]
        for yy, xx in pts:
            box[yy-y0][xx-x0] = c
        shapes[t] = (c, box)
    d_c, d_b = shapes['diamond']
    l_c, l_b = shapes['line']
    s_c, s_b = shapes['square']
    p_c, p_b = shapes['plus']
    dh, dw = len(d_b), len(d_b[0])
    lh, lw = len(l_b), len(l_b[0])
    sh, sw = len(s_b), len(s_b[0])
    ph, pw = len(p_b), len(p_b[0])
    oy = (h - (dh + sh + 1)) // 2
    ox = (w - (dw + lw + 1)) // 2
    out = [[bg]*w for _ in range(h)]
    for y in range(dh):
        for x in range(dw):
            if d_b[y][x]:
                out[oy+y][ox+x] = d_c
    for y in range(lh):
        for x in range(lw):
            if l_b[y][x]:
                out[oy+y][ox+dw+1+x] = l_c
    sy = oy + dh + 1
    for y in range(sh):
        for x in range(sw):
            if s_b[y][x]:
                out[sy+y][ox+x] = s_c
    py = oy + dh + 1
    px = ox + dw + 1
    for y in range(ph):
        for x in range(pw):
            if p_b[y][x]:
                out[py+y][px+x] = p_c
    return out