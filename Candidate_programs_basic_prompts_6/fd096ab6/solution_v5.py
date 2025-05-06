def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    bg = 1
    from collections import defaultdict
    pts = defaultdict(list)
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != bg:
                pts[v].append((r, c))
    for v, P in pts.items():
        if len(P) >= 5:
            continue
        rmin = min(r for r, _ in P)
        rmax = max(r for r, _ in P)
        cmin = min(c for _, c in P)
        cmax = max(c for _, c in P)
        center_r = (rmin + rmax) // 2
        center_c = (cmin + cmax) // 2
        S = set(P)
        S.add((center_r, center_c))
        for r, c in P:
            dr = r - center_r
            dc = c - center_c
            if dr == 0 and dc != 0:
                ud = (0, dc // abs(dc))
                rd = (ud[1], -ud[0])
            elif dc == 0 and dr != 0:
                ud = (dr // abs(dr), 0)
                rd = (ud[1], -ud[0])
            elif abs(dr) == abs(dc):
                ud = (dr // abs(dr), dc // abs(dc))
                rd = (ud[1], -ud[0])
            else:
                ud = (0, 0)
                rd = (0, 0)
            for d in (ud, rd):
                rr, cc = center_r + d[0], center_c + d[1]
                if 0 <= rr < h and 0 <= cc < w:
                    S.add((rr, cc))
        for r, c in S:
            res[r][c] = v
    return res