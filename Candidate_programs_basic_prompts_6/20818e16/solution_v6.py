def solve(grid):
    R, C = len(grid), len(grid[0])
    bg = grid[0][0]
    from collections import defaultdict
    cells = defaultdict(list)
    for r in range(R):
        for c in range(C):
            v = grid[r][c]
            if v != bg:
                cells[v].append((r, c))
    shapes = []
    for v, pts in cells.items():
        rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
        r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
        shapes.append((len(pts), v, r0, r1, c0, c1, set(pts)))
    shapes.sort(reverse=True)
    _, bigv, br0, br1, bc0, bc1, bpts = shapes[0]
    h, w = br1 - br0 + 1, bc1 - bc0 + 1
    out = [[bigv] * w for _ in range(h)]
    for _, v, r0, r1, c0, c1, pts in shapes[1:]:
        dr, dc = r0 - br0, c0 - bc0
        for r, c in pts:
            rr, cc = r - br0, c - bc0
            if 0 <= rr < h and 0 <= cc < w:
                out[rr][cc] = v
    return out