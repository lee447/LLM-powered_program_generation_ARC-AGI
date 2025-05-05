def solve(grid):
    h, w = len(grid), len(grid[0])
    C = grid[0][0]
    bw = 0
    while bw < w and grid[0][bw] == C:
        bw += 1
    sep = 0
    while bw + sep < w and all(grid[r][bw + sep] == 0 for r in range(h)):
        sep += 1
    obj0 = bw + sep
    stripes = [r for r in range(h) if all(grid[r][c] == C for c in range(bw))]
    stripes.sort()
    bands = [(stripes[i] + 1, stripes[i + 1]) for i in range(len(stripes) - 1)]
    shapes = []
    for top, bot in bands:
        pts = [(r, c) for r in range(top, bot) for c in range(obj0, w) if grid[r][c] != 0]
        if not pts:
            continue
        col = grid[pts[0][0]][pts[0][1]]
        rs = [r for r, c in pts]
        cs = [c for r, c in pts]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        rel = [(r - r0, c - c0) for r, c in pts]
        shapes.append((col, r1 - r0 + 1, c1 - c0 + 1, rel))
    shapes = sorted(shapes, key=lambda x: (-len(x[3]), x[0]))
    out = [[C] * bw for _ in range(h)]
    for (top, bot), (col, ph, pw, rel) in zip(bands, shapes):
        co = (bw - pw + 1) // 2
        for dr, dc in rel:
            out[top + dr][co + dc] = col
    return out