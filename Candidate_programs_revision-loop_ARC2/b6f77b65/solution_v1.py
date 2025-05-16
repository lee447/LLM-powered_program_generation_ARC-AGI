def solve(grid):
    H, W = len(grid), len(grid[0])
    from math import atan2
    ccs = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                ccs.setdefault(v, []).append((r, c))
    ctr = ((H - 1) / 2.0, (W - 1) / 2.0)
    clist = []
    for v, pts in ccs.items():
        sr = sum(r for r, _ in pts) / len(pts)
        sc = sum(c for _, c in pts) / len(pts)
        ang = atan2(sr - ctr[0], sc - ctr[1])
        clist.append((ang, v, pts))
    clist.sort()
    L = len(clist)
    res = [[0]*W for _ in range(H)]
    for i, (_, v, pts) in enumerate(clist):
        _, _, tgt = clist[(i+1)%L]
        for (r0,c0), (r1,c1) in zip(sorted(pts), sorted(tgt)):
            res[r1][c1] = v
    return res