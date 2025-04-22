def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import deque
    cols = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v:
                cols.setdefault(v, set()).add((r, c))
    infos = []
    for v, pts in cols.items():
        vis = set()
        clusters = []
        for p in pts:
            if p not in vis:
                q = [p]
                comp = []
                vis.add(p)
                while q:
                    x, y = q.pop()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if (nx, ny) in pts and (nx, ny) not in vis:
                            vis.add((nx, ny)); q.append((nx, ny))
                clusters.append(comp)
        def classify(comp):
            rs = [p[0] for p in comp]; cs = [p[1] for p in comp]
            r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
            h0, w0 = r1-r0+1, c1-c0+1
            return (len(comp)==h0*w0, r0, c0, h0, w0, r0, c0)
        clinfo = [classify(c) for c in clusters]
        sq = next(x for x in clinfo if x[0])
        br = next(x for x in clinfo if not x[0])
        _, sq_r0, sq_c0, sq_h, sq_w, _, _ = sq
        _, br_r0, br_c0, br_h, br_w, _, _ = br
        sq_set = set((r-sq_r0, c-sq_c0) for r,c in clusters[clinfo.index(sq)])
        br_set = set((r-br_r0, c-br_c0) for r,c in clusters[clinfo.index(br)])
        infos.append((sq_c0, v, sq_set, sq_h, sq_w, br_set, br_h, br_w))
    infos.sort(key=lambda x: x[0])
    out = [[0]*w for _ in range(h)]
    _, v1, sq1, sh1, sw1, br1, bh1, bw1 = infos[0]
    _, v2, sq2, sh2, sw2, br2, bh2, bw2 = infos[1]
    r_br = h-bh1
    r_sq = r_br-1-sh1+1
    for dr, dc in sq1:
        out[r_sq+dr][0+dc] = v1
    for dr, dc in br1:
        out[r_br+dr][0+dc] = v1
    r_br2 = h-bh2
    r_sq2 = r_br2-1-sh2+1
    c_sq2 = w-sw2
    c_br2 = w-bw2
    for dr, dc in sq2:
        out[r_sq2+dr][c_sq2+dc] = v2
    for dr, dc in br2:
        out[r_br2+dr][c_br2+dc] = v2
    return out