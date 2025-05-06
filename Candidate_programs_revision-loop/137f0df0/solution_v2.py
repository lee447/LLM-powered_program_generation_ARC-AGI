def solve(grid):
    h = len(grid)
    w = len(grid[0])
    cnt = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0:
                cnt[v] = cnt.get(v, 0) + 1
    block_color = max(cnt, key=cnt.get) if cnt else None
    def clusters(idxs):
        segs = []
        s = p = idxs[0]
        for x in idxs[1:]:
            if x == p + 1:
                p = x
            else:
                segs.append((s, p))
                s = p = x
        segs.append((s, p))
        return segs
    block_rows = [r for r in range(h) if any(grid[r][c] == block_color for c in range(w))]
    brc = clusters(block_rows)
    block_cols = [c for c in range(w) if any(grid[r][c] == block_color for r in range(h))]
    bcc = clusters(block_cols)
    inner_row = set()
    for i in range(len(brc) - 1):
        for r in range(brc[i][1] + 1, brc[i+1][0]):
            inner_row.add(r)
    outer_top = set(range(0, brc[0][0]))
    outer_bot = set(range(brc[-1][1] + 1, h))
    stripe_cols = []
    for i in range(len(bcc) - 1):
        s = bcc[i][1] + 1
        e = bcc[i+1][0] - 1
        if s <= e:
            stripe_cols.append((s, e))
    out = [row[:] for row in grid]
    s2, s1 = 2, 1
    min_bc = bcc[0][0]
    max_bc = bcc[-1][1]
    for r in inner_row:
        for c in range(w):
            out[r][c] = s2 if min_bc <= c <= max_bc else s1
    for s, e in stripe_cols:
        for c in range(s, e+1):
            for r in range(h):
                if any(r0 <= r <= r1 for r0, r1 in brc):
                    out[r][c] = s2
                elif r in outer_top or r in outer_bot:
                    out[r][c] = s1
    return out