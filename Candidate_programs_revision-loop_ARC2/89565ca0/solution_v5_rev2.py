from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    rects = []
    for v in range(1, 10):
        pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == v]
        if not pts:
            continue
        r0 = min(r for r, _ in pts)
        r1 = max(r for r, _ in pts)
        c0 = min(c for _, c in pts)
        c1 = max(c for _, c in pts)
        if r0 == r1 and c0 == c1:
            continue
        ok = True
        if r0 == r1:
            for c in range(c0, c1 + 1):
                if grid[r0][c] != v:
                    ok = False
                    break
        elif c0 == c1:
            for r in range(r0, r1 + 1):
                if grid[r][c0] != v:
                    ok = False
                    break
        else:
            for c in range(c0, c1 + 1):
                if grid[r0][c] != v or grid[r1][c] != v:
                    ok = False
                    break
            if ok:
                for r in range(r0, r1 + 1):
                    if grid[r][c0] != v or grid[r][c1] != v:
                        ok = False
                        break
        if ok:
            rects.append((v, r0, r1, c0, c1))
    r_b = set()
    c_b = set()
    for _, r0, r1, c0, c1 in rects:
        r_b.add(r0)
        r_b.add(r1)
        c_b.add(c0)
        c_b.add(c1)
    rs = sorted(r_b)
    cs = sorted(c_b)
    hr = [(rs[i], rs[i+1]) for i in range(len(rs) - 1) if rs[i+1] - rs[i] > 1]
    hc = [(cs[i], cs[i+1]) for i in range(len(cs) - 1) if cs[i+1] - cs[i] > 1]
    out = []
    for r0, r1 in hr:
        row = []
        for c0, c1 in hc:
            cnt = {}
            for r in range(r0 + 1, r1):
                for c in range(c0 + 1, c1):
                    v = grid[r][c]
                    if v:
                        cnt[v] = cnt.get(v, 0) + 1
            row.append(max(cnt, key=cnt.get) if cnt else 0)
        out.append(row)
    return out