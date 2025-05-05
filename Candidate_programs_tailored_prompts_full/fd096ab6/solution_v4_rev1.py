def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import Counter, defaultdict
    cnt = Counter(c for row in grid for c in row)
    bg = cnt.most_common(1)[0][0]
    color_pts = defaultdict(list)
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != bg:
                color_pts[c].append((i, j))
    template_color = max((c for c in color_pts if c != bg), key=lambda c: len(color_pts[c]))
    T = color_pts[template_color]
    def orient(pt, rot, ref):
        y, x = pt
        for _ in range(rot):
            y, x = -x, y
        if ref:
            x = -x
        return (y, x)
    results = {}
    for c, pts in color_pts.items():
        for rot in range(4):
            for ref in (False, True):
                O = [orient(p, rot, ref) for p in T]
                Oset = set(O)
                found = False
                for op in O:
                    for ip in pts:
                        dy = ip[0] - op[0]
                        dx = ip[1] - op[1]
                        S = {(oy + dy, ox + dx) for oy, ox in O}
                        if all((py, px) in S for py, px in pts):
                            results[c] = S
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            if c in results:
                break
    res = [row[:] for row in grid]
    for c, S in results.items():
        for i, j in S:
            if 0 <= i < h and 0 <= j < w:
                res[i][j] = c
    return res