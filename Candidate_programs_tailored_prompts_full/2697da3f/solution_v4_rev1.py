def solve(grid):
    h0 = len(grid)
    w0 = len(grid[0])
    pts = [(r, c) for r in range(h0) for c in range(w0) if grid[r][c] != 0]
    if not pts:
        return grid
    rs = [r for r, c in pts]
    cs = [c for r, c in pts]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    h = r1 - r0 + 1
    w = c1 - c0 + 1
    block = [[grid[r0 + i][c0 + j] for j in range(w)] for i in range(h)]
    def rot_cw(m):
        return [list(row) for row in zip(*m[::-1])]
    rot0 = block
    rot90 = rot_cw(block)
    rot180 = rot_cw(rot90)
    rot270 = rot_cw(rot180)
    s = 1 if w > h else 0
    step_y = h + s
    step_x = w + s
    out_n = 3 * h + 2 * s
    out = [[0] * out_n for _ in range(out_n)]
    for dy, dx, m in ((1, 0, rot0), (0, 1, rot90), (1, 2, rot180), (2, 1, rot270)):
        oy = dy * step_y
        ox = dx * step_x
        mh = len(m)
        mw = len(m[0])
        for i in range(mh):
            for j in range(mw):
                if m[i][j] != 0:
                    y = oy + i
                    x = ox + j
                    if 0 <= y < out_n and 0 <= x < out_n:
                        out[y][x] = m[i][j]
    return out