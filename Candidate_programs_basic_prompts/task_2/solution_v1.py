def solve(grid):
    h, w = len(grid), len(grid[0])
    freq = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v:
                freq.setdefault(v, []).append((i, j))
    def rect_info(pts):
        rs = [r for r, _ in pts]; cs = [c for _, c in pts]
        r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
        return r0, r1, c0, c1, (r1 - r0 + 1) * (c1 - c0 + 1) == len(pts)
    marker = None
    best = 0
    for v, pts in freq.items():
        r0, r1, c0, c1, ok = rect_info(pts)
        if ok and (r1 - r0 + 1) * (c1 - c0 + 1) > best:
            best = (r1 - r0 + 1) * (c1 - c0 + 1)
            marker = (r0, r1, c0, c1)
    if not marker:
        return []
    r0, r1, c0, c1 = marker
    mh = r1 - r0 + 1
    if r0 - mh >= 0:
        sr = r0 - mh
    else:
        sr = r1 + 1
    out = []
    for i in range(sr, sr + mh):
        out.append(grid[i][c0:c1+1])
    return out