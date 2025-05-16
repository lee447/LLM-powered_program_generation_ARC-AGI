from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    rects = []
    for c in set(v for row in grid for v in row if v != 0):
        pts = [(y, x) for y in range(h) for x in range(w) if grid[y][x] == c]
        if not pts: continue
        ys = [y for y, x in pts]; xs = [x for y, x in pts]
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
    def segment(r):
        miny, maxy, minx, maxx, c = r
        ys = range(miny+1, maxy)
        w_in = maxx - minx - 1
        base, rem = divmod(w_in, 4)
        widths = [base + (i < rem) for i in range(4)]
        x0 = minx + 1
        row = []
        for bw in widths:
            seg = []
            for y in ys:
                for x in range(x0, x0 + bw):
                    v = grid[y][x]
                    if v != 0 and v != c:
                        seg.append(v)
            row.append(max(set(seg), key=seg.count) if seg else c)
            x0 += bw
        return row
    rows = [segment(r) for r in rects]
    def keyfn(row):
        an = sum(1 for v in row if v != row[0])
        return (-an, row[0])
    rows.sort(key=keyfn)
    return rows