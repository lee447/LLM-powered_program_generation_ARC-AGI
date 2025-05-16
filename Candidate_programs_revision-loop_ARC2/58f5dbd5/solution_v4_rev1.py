from collections import Counter
def solve(grid):
    h, w = len(grid), len(grid[0])
    border = grid[0][0]
    row_b = [i for i in range(h) if all(grid[i][j] == border for j in range(w))]
    col_b = [j for j in range(w) if all(grid[i][j] == border for i in range(h))]
    def collapse(b):
        runs, cur = [], []
        for x in b:
            if not cur or x == cur[-1] + 1:
                cur.append(x)
            else:
                runs.append(cur); cur = [x]
        if cur: runs.append(cur)
        return runs
    def nat_segs(b, n):
        runs = collapse(b)
        s = []
        for i in range(len(runs) - 1):
            e = runs[i][-1] + 1
            s.append((runs[i][-1] + 1, runs[i+1][0] - 1))
        return s
    nr = nat_segs(row_b, h)
    nc = nat_segs(col_b, w)
    a, b = min(row_b) + 1, max(row_b) - 1
    c, d = min(col_b) + 1, max(col_b) - 1
    H = b - a + 1
    W = d - c + 1
    k = max(len(nr), len(nc))
    def split(a, L, k):
        sz = L // k
        return [(a + i*sz, a + (i+1)*sz - 1) for i in range(k)]
    rsegs = nr if len(nr) == k else split(a, H, k)
    csegs = nc if len(nc) == k else split(c, W, k)
    orient = 'col' if len(nr) < len(nc) else 'row'
    prim = csegs if orient == 'col' else rsegs
    oth = rsegs if orient == 'col' else csegs
    best, best_score = 0, -1
    for i, (x0, x1) in enumerate(prim):
        cnt = 0
        for (y0, y1) in oth:
            found = False
            for r in (range(y0, y1+1) if orient=='col' else range(x0, x1+1)):
                for s in (range(x0, x1+1) if orient=='col' else range(y0, y1+1)):
                    if orient=='col':
                        if grid[r][s] != border:
                            found = True; break
                    else:
                        if grid[s][r] != border:
                            found = True; break
                if found: break
            if found: cnt += 1
        length = x1 - x0 + 1
        score = cnt * length
        if score > best_score:
            best_score = score; best = i
    panels = []
    if orient == 'col':
        cx0, cx1 = prim[best]
        for (ry0, ry1) in oth:
            p = [row[cx0:cx1+1] for row in grid[ry0:ry1+1]]
            panels.append(p)
    else:
        ry0, ry1 = prim[best]
        for (cx0, cx1) in oth:
            p = [row[cx0:cx1+1] for row in grid[ry0:ry1+1]]
            panels.append(p)
    max_h = max(len(p) for p in panels)
    max_w = max(len(p[0]) for p in panels)
    def pad(p):
        h0, w0 = len(p), len(p[0])
        dh = max_h - h0
        dw = max_w - w0
        top, bot = dh//2, dh - dh//2
        left, right = dw//2, dw - dw//2
        cnt = Counter(v for row in p for v in row if v != border)
        col = cnt.most_common(1)[0][0] if cnt else border
        res = [[col]*max_w for _ in range(top)]
        for row in p:
            res.append([col]*left + row + [col]*right)
        for _ in range(bot):
            res.append([col]*max_w)
        return res
    P = [pad(p) for p in panels]
    out = []
    if orient == 'row':
        width = max_w*len(P) + len(P) + 1
        brow = [border]*width
        out.append(brow)
        for i in range(max_h):
            row = [border]
            for p in P:
                row += p[i] + [border]
            out.append(row)
        out.append(brow)
    else:
        width = max_w + 2
        brow = [border]*width
        out.append(brow)
        for p in P:
            for row in p:
                out.append([border] + row + [border])
            out.append(brow)
    return out