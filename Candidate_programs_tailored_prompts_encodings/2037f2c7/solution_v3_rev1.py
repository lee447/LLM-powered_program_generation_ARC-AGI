from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    # collect non-zero values positions
    vals = {}
    for i in range(n):
        for j in range(m):
            v = grid[i][j]
            if v != 0:
                vals.setdefault(v, []).append((i, j))
    # find stripe color
    best = None
    for v, cells in vals.items():
        cols = {j for _, j in cells}
        rows = {i for i, _ in cells}
        if len(cols) <= 2 and len(rows) > 1:
            score = (len(rows), -len(cols))
            if best is None or score > best[0]:
                best = (score, v, sorted(cols), sorted(rows))
    if best is None:
        return [[]]
    _, stripe_color, stripe_cols, stripe_rows = best
    # pick contiguous stripe block
    groups = []
    tmp = [stripe_cols[0]]
    for x in stripe_cols[1:]:
        if x == tmp[-1] + 1:
            tmp.append(x)
        else:
            groups.append(tmp)
            tmp = [x]
    groups.append(tmp)
    stripe_cols = groups[0]
    sc0, sc1 = stripe_cols[0], stripe_cols[-1]
    # top/mid/bottom rows
    r0, r1 = stripe_rows[0], stripe_rows[-1]
    mids = [r0] if len(stripe_cols) == 1 else [r0, r1]
    rows = [r0 - 1] + mids + [r1 + 1]
    # find horizontal span from stripe row r0
    nz = [j for j in range(m) if grid[r0][j] != 0]
    c0, c1 = min(nz), max(nz)
    h = len(rows)
    w = c1 - c0 + 1
    out = [[0] * w for _ in range(h)]
    for oi, r in enumerate(rows):
        arr = [False] * m
        for j in range(c0, c1 + 1):
            if grid[r][j] != 0 and j not in stripe_cols:
                arr[j] = True
        if oi == 0 or oi == h - 1:
            out[oi][0] = 8
            out[oi][w - 1] = 8
        else:
            j = c0
            while j <= c1:
                if arr[j]:
                    s = j
                    while j <= c1 and arr[j]:
                        j += 1
                    e = j - 1
                    out[oi][s - c0] = 8
                    out[oi][e - c0] = 8
                else:
                    j += 1
    return out