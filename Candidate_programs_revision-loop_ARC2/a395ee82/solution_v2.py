def solve(grid):
    h, w = len(grid), len(grid[0])
    colors = {}
    for i in range(h):
        for j in range(w):
            colors.setdefault(grid[i][j], 0)
            colors[grid[i][j]] += 1
    bg = max(colors, key=lambda c: colors[c])
    pts = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != bg:
                pts.setdefault(c, []).append((i, j))
    cols = list(pts.keys())
    c1, c2 = cols[0], cols[1] if len(cols) > 1 else cols[0]
    def bbox(ps):
        rs = [p[0] for p in ps]; cs = [p[1] for p in ps]
        return min(rs), max(rs), min(cs), max(cs)
    r1min, r1max, c1min, c1max = bbox(pts[c1])
    r2min, r2max, c2min, c2max = bbox(pts[c2])
    bh1, bw1 = r1max - r1min + 1, c1max - c1min + 1
    bh2, bw2 = r2max - r2min + 1, c2max - c2min + 1
    sub1 = [row[c1min:c1min + bw1] for row in grid[r1min:r1min + bh1]]
    sub2 = [row[c2min:c2min + bw2] for row in grid[r2min:r2min + bh2]]
    out = [list(row) for row in grid]
    for di in range(bh1):
        for dj in range(bw1):
            if di < bh2 and dj < bw2:
                out[r1min + di][c1min + dj] = sub2[di][dj]
    for di in range(bh2):
        for dj in range(bw2):
            if di < bh1 and dj < bw1:
                out[r2min + di][c2min + dj] = sub1[di][dj]
    return out