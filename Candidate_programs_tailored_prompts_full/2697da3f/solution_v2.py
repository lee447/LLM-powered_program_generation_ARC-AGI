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
    motif = [(r - r0, c - c0, grid[r][c]) for r, c in pts]
    s = 1 if w > h else 0
    step_y = h + s
    step_x = w + s
    out_n = 3 * h + 2 * s
    out = [[0] * out_n for _ in range(out_n)]
    for dy in range(3):
        for dx in range(3):
            oy = dy * step_y
            ox = dx * step_x
            for ry, cx, v in motif:
                y = oy + ry
                x = ox + cx
                if 0 <= y < out_n and 0 <= x < out_n:
                    out[y][x] = v
    return out