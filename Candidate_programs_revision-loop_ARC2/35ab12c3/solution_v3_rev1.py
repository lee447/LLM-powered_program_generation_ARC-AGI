from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    pos = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c:
                pos.setdefault(c, []).append((i, j))
    out = [[0]*w for _ in range(h)]
    used = set()

    def draw_diamond(center, r, border, fill):
        ci, cj = center
        for i in range(h):
            for j in range(w):
                d = abs(i-ci) + abs(j-cj)
                if d == r and out[i][j] == 0:
                    out[i][j] = border
                elif d < r and fill is not None and out[i][j] == 0:
                    out[i][j] = fill

    def draw_line(a, b, color):
        (r1, c1), (r2, c2) = a, b
        if r1 == r2:
            for j in range(min(c1, c2), max(c1, c2) + 1):
                out[r1][j] = color
        else:
            for i in range(min(r1, r2), max(r1, r2) + 1):
                out[i][c1] = color

    def draw_rect(rmin, rmax, cmin, cmax, border, fill):
        for j in range(cmin, cmax+1):
            if out[rmin][j] == 0: out[rmin][j] = border
            if out[rmax][j] == 0: out[rmax][j] = border
        for i in range(rmin, rmax+1):
            if out[i][cmin] == 0: out[i][cmin] = border
            if out[i][cmax] == 0: out[i][cmax] = border
        if fill is not None:
            for i in range(rmin+1, rmax):
                for j in range(cmin+1, cmax):
                    if out[i][j] == 0:
                        out[i][j] = fill

    # diamond: one single, one multi (>1)
    singles = [c for c, pts in pos.items() if len(pts) == 1]
    multis = [c for c, pts in pos.items() if len(pts) > 1]
    if len(singles) == 1 and multis:
        d = singles[0]
        # choose fill as the multi with smallest count
        fill = min(multis, key=lambda c: len(pos[c]))
        ci, cj = pos[d][0]
        # radius = max distance from center to all fill pts
        r = max(abs(ci - fi) + abs(cj - fj) for fi, fj in pos[fill])
        draw_diamond((ci, cj), r, d, fill)
        used.add(d)
        used.add(fill)

    # straight lines for pairs
    for c, pts in pos.items():
        if c not in used and len(pts) == 2:
            a, b = pts
            if a[0] == b[0] or a[1] == b[1]:
                draw_line(a, b, c)
                used.add(c)

    # rectangle1: one color at 4 corners, another single
    for c, pts in pos.items():
        if c not in used and len(pts) == 4:
            rs = [i for i, _ in pts]
            cs = [j for _, j in pts]
            rmin, rmax = min(rs), max(rs)
            cmin, cmax = min(cs), max(cs)
            corners = {(rmin, cmin), (rmin, cmax), (rmax, cmin), (rmax, cmax)}
            if set(pts) == corners:
                others = [d for d in pos if d not in used and d != c and len(pos[d]) == 1]
                if others:
                    d = others[0]
                    draw_rect(rmin, rmax, cmin, cmax, d, c)
                    used.add(c)
                    used.add(d)

    # rectangle-other: one single and one big (>3)
    singles = [c for c, pts in pos.items() if c not in used and len(pts) == 1]
    bigs = [c for c, pts in pos.items() if c not in used and len(pts) > 3]
    if len(singles) == 1 and len(bigs) == 1:
        d = singles[0]
        c = bigs[0]
        pts = pos[c] + pos[d]
        rows = [i for i, _ in pts]
        cols = [j for _, j in pts]
        rmin, rmax = min(rows), max(rows)
        cmin, cmax = min(cols), max(cols)
        draw_rect(rmin, rmax, cmin, cmax, d, c)
        used.add(c)
        used.add(d)

    # overlay originals
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0:
                out[i][j] = grid[i][j]
    return out