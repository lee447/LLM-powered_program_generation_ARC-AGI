def solve(grid):
    R, C = len(grid), len(grid[0])
    pos = {}
    for i in range(R):
        for j in range(C):
            v = grid[i][j]
            pos.setdefault(v, []).append((i, j))
    mask_color = None
    mask_rect = None
    max_area = 0
    for v, cells in pos.items():
        n = len(cells)
        if n <= 1:
            continue
        rs = [r for r, _ in cells]
        cs = [c for _, c in cells]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        area = (r1 - r0 + 1) * (c1 - c0 + 1)
        if area == n and area < R * C and area > max_area:
            max_area = area
            mask_color = v
            mask_rect = (r0, r1, c0, c1)
    r0, r1, c0, c1 = mask_rect
    h, w = r1 - r0 + 1, c1 - c0 + 1
    sig_counts = {}
    for i in range(R - h + 1):
        for j in range(C - w + 1):
            if not (i > r1 or i + h - 1 < r0 or j > c1 or j + w - 1 < c0):
                continue
            ok = True
            flat = []
            for di in range(h):
                row = grid[i + di]
                for dj in range(w):
                    v = row[j + dj]
                    if v == mask_color:
                        ok = False
                        break
                    flat.append(v)
                if not ok:
                    break
            if not ok:
                continue
            t = tuple(flat)
            sig_counts[t] = sig_counts.get(t, 0) + 1
    best = max(sig_counts.items(), key=lambda x: x[1])[0]
    res = []
    for i in range(h):
        res.append(list(best[i * w:(i + 1) * w]))
    return res