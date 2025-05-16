import copy
def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = {}
    for i in range(h):
        for j in range(w):
            counts[grid[i][j]] = counts.get(grid[i][j], 0) + 1
    bg = max(counts, key=counts.get)
    pts = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != bg:
                pts.setdefault(c, []).append((i, j))
    if len(pts) != 2:
        return grid
    (c1, c2) = list(pts.keys())
    def bbox(ps):
        rs = [p[0] for p in ps]
        cs = [p[1] for p in ps]
        return min(rs), max(rs), min(cs), max(cs)
    r1min, r1max, c1min, c1max = bbox(pts[c1])
    r2min, r2max, c2min, c2max = bbox(pts[c2])
    offs1 = [(r - r1min, c - c1min) for (r, c) in pts[c1]]
    offs2 = [(r - r2min, c - c2min) for (r, c) in pts[c2]]
    out = copy.deepcopy(grid)
    for r, c in pts[c1]:
        out[r][c] = bg
    for r, c in pts[c2]:
        out[r][c] = bg
    for dr, dc in offs1:
        out[r2min + dr][c2min + dc] = c1
    for dr, dc in offs2:
        out[r1min + dr][c1min + dc] = c2
    return out