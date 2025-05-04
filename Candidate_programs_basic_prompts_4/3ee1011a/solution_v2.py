def solve(grid):
    bounds = {}
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if v:
                if v not in bounds:
                    bounds[v] = [r, r, c, c]
                else:
                    b = bounds[v]
                    if r < b[0]: b[0] = r
                    if r > b[1]: b[1] = r
                    if c < b[2]: b[2] = c
                    if c > b[3]: b[3] = c
    shapes = []
    for color, (r0, r1, c0, c1) in bounds.items():
        h = r1 - r0 + 1
        w = c1 - c0 + 1
        shapes.append((max(h, w), color))
    if not shapes:
        return []
    shapes.sort(key=lambda x: x[0], reverse=True)
    s0 = shapes[0][0]
    res = [[shapes[0][1]] * s0 for _ in range(s0)]
    for i in range(1, len(shapes)):
        c = shapes[i][1]
        off = i
        sz = s0 - 2 * off
        for r in range(off, off + sz):
            for cc in range(off, off + sz):
                res[r][cc] = c
    return res