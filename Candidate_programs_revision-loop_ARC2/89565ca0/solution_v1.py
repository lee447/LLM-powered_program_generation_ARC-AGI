def solve(grid):
    def find_rects():
        rects = {}
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v != 0:
                    if v not in rects:
                        rects[v] = [r, r, c, c]
                    else:
                        rects[v][0] = min(rects[v][0], r)
                        rects[v][1] = max(rects[v][1], r)
                        rects[v][2] = min(rects[v][2], c)
                        rects[v][3] = max(rects[v][3], c)
        B = []
        for v, (r0, r1, c0, c1) in rects.items():
            ok = True
            for r in range(r0, r1+1):
                for c in range(c0, c1+1):
                    if not (grid[r][c] == v and (r in (r0, r1) or c in (c0, c1)) or grid[r][c] != v and (r not in (r0, r1) and c not in (c0, c1))):
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                B.append((v, r0, r1, c0, c1))
        return B
    R = find_rects()
    outer = max(R, key=lambda x: (x[3]-x[4], x[2]-x[1]))
    rs = set()
    cs = set()
    for v, r0, r1, c0, c1 in R:
        rs.add(r0); rs.add(r1)
        cs.add(c0); cs.add(c1)
    rs = sorted(rs)
    cs = sorted(cs)
    hr = [(rs[i], rs[i+1]) for i in range(len(rs)-1)]
    hc = [(cs[i], cs[i+1]) for i in range(len(cs)-1)]
    hr = hr[1:-1]
    hc = hc[1:-1]
    out = []
    for r0, r1 in hr:
        row = []
        for c0, c1 in hc:
            cnt = {}
            for r in range(r0, r1+1):
                for c in range(c0, c1+1):
                    v = grid[r][c]
                    if v:
                        cnt[v] = cnt.get(v, 0) + 1
            if cnt:
                row.append(max(cnt, key=cnt.get))
            else:
                row.append(0)
        out.append(row)
    return out