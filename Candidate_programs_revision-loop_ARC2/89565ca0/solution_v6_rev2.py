from typing import List
from collections import Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    rects = []
    colors = set(v for row in grid for v in row if v)
    for c in colors:
        pts = [(y, x) for y in range(h) for x in range(w) if grid[y][x] == c]
        if not pts: continue
        ys = [y for y, _ in pts]; xs = [x for _, x in pts]
        miny, maxy, minx, maxx = min(ys), max(ys), min(xs), max(xs)
        if maxy - miny < 2 or maxx - minx < 2: continue
        perim = []
        for x0 in range(minx, maxx+1):
            perim.append((miny, x0)); perim.append((maxy, x0))
        for y0 in range(miny+1, maxy):
            perim.append((y0, minx)); perim.append((y0, maxx))
        total = len(perim)
        cnt = sum(1 for y0, x0 in perim if grid[y0][x0] == c)
        if cnt / total >= 0.8:
            rects.append((miny, maxy, minx, maxx, c))
    rects.sort(key=lambda r: (r[1]-r[0])*(r[3]-r[2]))
    
    rows = []
    for i, (miny, maxy, minx, maxx, c) in enumerate(rects):
        ys = range(miny+1, maxy)
        xs = maxx - minx - 1
        base, rem = divmod(xs, 4)
        widths = [base + (j < rem) for j in range(4)]
        # determine fill color
        fill_cnt = Counter()
        for y in ys:
            for x in range(minx+1, maxx):
                v = grid[y][x]
                if v and v != c:
                    fill_cnt[v] += 1
        f = fill_cnt.most_common(1)[0][0] if fill_cnt else c
        x0 = minx + 1
        stripe = []
        got_fill = False
        for wseg in widths:
            seg = []
            for y in ys:
                for x in range(x0, x0 + wseg):
                    v = grid[y][x]
                    if v and v != c:
                        seg.append(v)
            if seg:
                col = Counter(seg).most_common(1)[0][0]
                stripe.append(col)
                if col != c:
                    got_fill = True
            else:
                stripe.append(f if got_fill or stripe else c)
            x0 += wseg
        rows.append(stripe)

    rows.sort(key=lambda r: (-sum(1 for v in r if v != r[0]), r[0]))
    return rows