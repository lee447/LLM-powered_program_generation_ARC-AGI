from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cnt = {}
    for row in grid:
        for c in row:
            cnt[c] = cnt.get(c, 0) + 1
    bg = max(cnt, key=lambda c: cnt[c])
    bar = min((c for c in cnt if c != bg), key=lambda c: cnt[c])
    shape = max((c for c in cnt if c not in (bg, bar)), key=lambda c: cnt[c])
    inv = next((c for c in (3, 4) if c not in (bg, bar, shape)), None)
    if inv is None:
        inv = next(c for c in range(10) if c not in (bg, bar, shape))
    bcoords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == bar]
    brow = sorted({r for r, _ in bcoords})
    bcol = sorted({c for _, c in bcoords})
    ori = 'H' if len(brow) == 1 else 'V'
    scoords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == shape]
    shape_rows = sorted({r for r, _ in scoords})
    shape_cols = sorted({c for _, c in scoords})
    srmin, srmax = shape_rows[0], shape_rows[-1]
    scmin, scmax = shape_cols[0], shape_cols[-1]
    tr = (srmin + srmax) / 2
    cr = min(shape_rows, key=lambda r: abs(r - tr))
    tc = (scmin + scmax) / 2
    cc = min(shape_cols, key=lambda c: abs(c - tc))
    hr = sorted(c for r, c in scoords if r == cr)
    hc0, hc1 = (hr[0], hr[-1]) if hr else (scmin, scmax)
    vr = sorted(r for r, c in scoords if c == cc)
    vc0, vc1 = (vr[0], vr[-1]) if vr else (srmin, srmax)
    if ori == 'H':
        r1, r2 = srmin + 1, srmax - 1
        rs, cs = [r1, r2], bcol
    else:
        c1, c2 = scmin + 1, scmax - 1
        rs, cs = brow, [c1, c2]
    out = [row[:] for row in grid]
    for r in rs:
        if 0 <= r < h:
            for c in cs:
                if 0 <= c < w:
                    out[r][c] = bar
    for c in range(hc0, hc1 + 1):
        if 0 <= c < w:
            out[cr][c] = inv
    for r in range(vc0, vc1 + 1):
        if 0 <= r < h:
            out[r][cc] = inv
    if ori == 'H':
        cd = 'S' if brow[0] > tr else 'N'
        for d, rr in [('N', 0), ('S', h - 1)]:
            for c in bcol:
                out[rr][c] = bar if d == cd else inv
    else:
        cd = 'E' if bcol[0] > tc else 'W'
        for d, c0 in [('W', 0), ('E', w - 1)]:
            for r in brow:
                out[r][c0] = bar if d == cd else inv
    return out