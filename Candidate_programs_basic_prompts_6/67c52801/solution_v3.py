def solve(grid):
    h = len(grid)
    w = len(grid[0])
    base_row = None
    base_color = None
    for r in range(h-1, -1, -1):
        row = grid[r]
        if row[0] != 0 and all(x == row[0] for x in row):
            base_row = r
            base_color = row[0]
            break
    out = [[0]*w for _ in range(h)]
    if base_row is not None:
        out[base_row] = list(grid[base_row])
        if base_row >= 1:
            out[base_row-1] = list(grid[base_row-1])
    shapes = {}
    for r in range(h):
        if r == base_row: continue
        for c in range(w):
            v = grid[r][c]
            if v != 0 and v != base_color:
                shapes.setdefault(v, []).append((r, c))
    even = []
    odd = []
    for v, pts in shapes.items():
        cnt = len(pts)
        if cnt % 2 == 0:
            even.append((v, cnt))
        else:
            odd.append((v, pts))
    odd = odd
    even.sort(key=lambda x: x[1])
    # place odd shapes
    for v, pts in odd:
        row = base_row - 1
        for _, c in pts:
            out[row][c] = v
    # place even shapes
    m = len(even)
    if m > 0:
        widths = [cnt//2 for _, cnt in even]
        total_w = sum(widths)
        if m == 1:
            gaps = [1, 1]
        else:
            gaps = m + 1
            empty = w - total_w
            base_gap = empty // gaps
            extra = empty % gaps
            gaps = [base_gap + (i >= (gaps - extra)) for i in range(gaps)]
        if m == 1:
            curr = 1
            vs = [even[0][0]]
            ws = [widths[0]]
            gs = [gaps[0], gaps[1]]
        else:
            curr = gaps[0]
            vs = [v for v, _ in even]
            ws = widths
            gs = gaps
        for i, v in enumerate(vs):
            wi = ws[i]
            hi = 2
            top = base_row - hi
            for dr in range(hi):
                for dc in range(wi):
                    out[top+dr][curr+dc] = v
            curr += wi + gs[i+1]
    return out