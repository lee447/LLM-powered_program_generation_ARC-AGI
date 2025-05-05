def solve(grid):
    from math import atan2
    from statistics import median
    h, w = len(grid), len(grid[0])
    blocks = []
    for i in range(h - 1):
        for j in range(w - 1):
            if grid[i][j] == 2 and grid[i][j+1] == 2 and grid[i+1][j] == 2 and grid[i+1][j+1] == 2:
                blocks.append((i, j))
    if not blocks:
        return grid
    rs = sorted(r for r, c in blocks)
    cs = sorted(c for r, c in blocks)
    cr = int(median(rs))
    cc = int(median(cs))
    pts = []
    for r, c in blocks:
        dr = r - cr
        dc = c - cc
        ang = atan2(dr, dc) % (2 * 3.141592653589793)
        dist = dr*dr + dc*dc
        pts.append([r, c, ang, dist, None])
    K = min(3, len(pts))
    centers = [(2*3.141592653589793*i)/K for i in range(K)]
    for _ in range(10):
        for p in pts:
            best = min(range(K), key=lambda k: abs((p[2] - centers[k] + 3.141592653589793) % (2*3.141592653589793) - 3.141592653589793))
            p[4] = best
        for k in range(K):
            cl = [p[2] for p in pts if p[4] == k]
            if cl:
                avg = sum(cl) / len(cl)
                centers[k] = avg
    to_highlight = set()
    for k in range(K):
        grp = [p for p in pts if p[4] == k]
        grp.sort(key=lambda x: x[3], reverse=True)
        for p in grp[:2]:
            to_highlight.add((p[0], p[1]))
    out = [row[:] for row in grid]
    for r, c in to_highlight:
        for dr in (0,1):
            for dc in (0,1):
                out[r+dr][c+dc] = 8
    return out