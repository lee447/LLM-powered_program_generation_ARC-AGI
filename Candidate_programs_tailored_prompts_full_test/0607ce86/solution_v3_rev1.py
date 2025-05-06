from collections import Counter

def solve(grid):
    n, m = len(grid), len(grid[0])
    row_counts = [sum(1 for v in row if v != 0) for row in grid]
    max_rc = max(row_counts)
    if max_rc == 0:
        return [[0]*m for _ in range(n)]
    thr_r = max_rc/2
    nzr = [i for i,c in enumerate(row_counts) if c > thr_r]
    bands = []
    for r in nzr:
        if not bands or r != bands[-1][-1] + 1:
            bands.append([r])
        else:
            bands[-1].append(r)
    first_band = bands[0]
    h = len(first_band)
    col_counts = [sum(1 for r in first_band if grid[r][c] != 0) for c in range(m)]
    thr_c = h/2
    cand = [c for c,cc in enumerate(col_counts) if cc > thr_c]
    segs = []
    if cand:
        s = cand[0]
        p = s
        for c in cand[1:]:
            if c == p + 1:
                p = c
            else:
                segs.append((s, p-s+1))
                s = c
                p = c
        segs.append((s, p-s+1))
    blocks = []
    for x,w in segs:
        b = [[grid[r][c] for c in range(x, x+w)] for r in first_band]
        blocks.append(b)
    prot = None
    for b in blocks:
        w = len(b[0])
        ok = True
        for i in range(h):
            for j in range(w):
                if b[i][j] != b[i][w-1-j]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            prot = [row[:] for row in b]
            break
    if prot is None:
        w0 = segs[0][1]
        prot = [[0]*w0 for _ in range(h)]
        for i in range(h):
            for j in range(w0):
                vals = [b[i][j] for b in blocks]
                prot[i][j] = Counter(vals).most_common(1)[0][0]
    out = [[0]*m for _ in range(n)]
    for band in bands:
        r0 = band[0]
        for x,w in segs:
            for i in range(h):
                for j in range(w):
                    out[r0+i][x+j] = prot[i][j]
    return out