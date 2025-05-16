from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cnt = {}
    for row in grid:
        for c in row:
            cnt[c] = cnt.get(c, 0) + 1
    bg = max(cnt, key=cnt.get)
    # find bar color: smallest count ≠ bg, shape
    others = sorted([(cnt[c], c) for c in cnt if c != bg])
    bar = others[0][1]
    # find shape color: largest count ≠ bg, bar
    shape = max([c for c in cnt if c not in (bg, bar)], key=lambda c: cnt[c])
    invs = [c for c in cnt if c not in (bg, bar, shape)]
    inv = invs[0] if invs else (3 if bar == 4 else 4)
    # bar coords
    bcoords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == bar]
    rows = {r for r, _ in bcoords}
    cols = {c for _, c in bcoords}
    ori = 'H' if len(rows) == 1 else 'V'
    # bounding of shape
    scoords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == shape]
    srmin = min(r for r, _ in scoords)
    srmax = max(r for r, _ in scoords)
    scmin = min(c for _, c in scoords)
    scmax = max(c for _, c in scoords)
    # bar direction
    if ori == 'H':
        brow = next(iter(rows))
        cd = 'S' if brow > (srmin + srmax)//2 else 'N'
        c0, c1 = min(cols), max(cols) + 1
    else:
        bcol = next(iter(cols))
        cd = 'E' if bcol > (scmin + scmax)//2 else 'W'
        r0, r1 = min(rows), max(rows) + 1
    out = [row[:] for row in grid]
    # internal cross
    cr = (srmin + srmax) // 2
    cc = (scmin + scmax) // 2
    for c in range(scmin, scmax+1):
        out[cr][c] = inv
    for r in range(srmin, srmax+1):
        out[r][cc] = inv
    # external bars
    if ori == 'H':
        for d, rr in (('N', 0), ('S', h-1)):
            col0 = c0
            for c in range(c0, c1):
                out[rr][c] = bar if d == cd else inv
    else:
        for d, cc0 in (('W', 0), ('E', w-1)):
            for r in range(r0, r1):
                out[r][cc0] = bar if d == cd else inv
    return out