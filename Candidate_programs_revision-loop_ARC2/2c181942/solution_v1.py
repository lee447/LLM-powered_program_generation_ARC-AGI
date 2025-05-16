def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = 8
    comps = {}
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c != bg:
                comps.setdefault(c, []).append((y, x))
    cs = list(comps.items())
    def avg_x(item):
        ysxs = item[1]
        return sum(x for y, x in ysxs) / len(ysxs)
    def key(item):
        pts = item[1]
        return (-len(pts), -avg_x(item))
    cs.sort(key=key)
    if len(cs) > 4:
        cs = cs[1:5]
    shapes = []
    for c, pts in cs:
        ys = [y for y, x in pts]
        xs = [x for y, x in pts]
        y0, y1 = min(ys), max(ys)
        x0, x1 = min(xs), max(xs)
        box = [[0] * (x1 - x0 + 1) for _ in range(y1 - y0 + 1)]
        for y, x in pts:
            box[y - y0][x - x0] = c
        shapes.append((c, box))
    # classify diamond by shape.count == max_count
    counts = [sum(row.count(c) for row in box) for c, box in shapes]
    idx = sorted(range(len(shapes)), key=lambda i: (-counts[i], -sum(x for y,x in comps[shapes[i][0]])) )
    arranged = [shapes[i] for i in idx]
    # place in cluster
    d_c, d_b = arranged[0]
    p_c, p_b = arranged[1]
    s_c, s_b = arranged[2]
    l_c, l_b = arranged[3]
    dh, dw = len(d_b), len(d_b[0])
    lh, lw = len(l_b), len(l_b[0])
    ph, pw = len(p_b), len(p_b[0])
    sh, sw = len(s_b), len(s_b[0])
    oy = (h - (dh + sh + 1)) // 2
    ox = (w - (dw + lw + pw + 1)) // 2
    out = [[bg] * w for _ in range(h)]
    # diamond TL
    for y in range(dh):
        for x in range(dw):
            if d_b[y][x]:
                out[oy + y][ox + x] = d_c
    # line top
    for y in range(lh):
        for x in range(lw):
            if l_b[y][x]:
                out[oy + y][ox + dw + x] = l_c
    # square bottom-left
    sy = oy + dh - sh
    for y in range(sh):
        for x in range(sw):
            if s_b[y][x]:
                out[sy + y][ox + x] = s_c
    # plus right
    py = oy + (dh - ph) // 2
    px = ox + dw + lw + 1
    for y in range(ph):
        for x in range(pw):
            if p_b[y][x]:
                out[py + y][px + x] = p_c
    return out