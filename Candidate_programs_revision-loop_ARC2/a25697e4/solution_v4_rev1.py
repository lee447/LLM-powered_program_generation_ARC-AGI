from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = max(set(x for row in grid for x in row),
             key=lambda c: sum(r.count(c) for r in grid))
    cols = [c for c in set(x for row in grid for x in row) if c != bg]
    counts = {c: sum(row.count(c) for row in grid) for c in cols}
    cols_sorted = sorted(cols, key=lambda c: counts[c])
    c_small, c_mid, c_large = cols_sorted[0], cols_sorted[1], cols_sorted[2]
    def bbox(color: int) -> Tuple[int,int,int,int]:
        rs = [i for i in range(h) for j in range(w) if grid[i][j] == color]
        cs = [j for i in range(h) for j in range(w) if grid[i][j] == color]
        return min(rs), min(cs), max(rs), max(cs)
    r0, c0, r3, c3 = bbox(c_large)
    r1, c1, r2, c2 = bbox(c_mid)
    r4, c4, r5, c5 = bbox(c_small)
    out = [row[:] for row in grid]
    # overlay mid into large
    th, tw = (r3 - r0), (c3 - c0 + 1)
    sh, sw = (r2 - r1 + 1), (c2 - c1 + 1)
    for i in range(r0+1, r3):
        for j in range(c0, c3+1):
            ii = int((i - (r0+1)) * sh / (r3 - r0 - 1) + 0.5)
            jj = int((j - c0) * sw / tw + 0.5)
            if 0 <= ii < sh and 0 <= jj < sw and grid[r1+ii][c1+jj] == c_mid:
                out[i][j] = c_mid
    # overlay small into mid
    th2, tw2 = (r2 - r1), (c2 - c1 + 1)
    sh2, sw2 = (r5 - r4 + 1), (c5 - c4 + 1)
    for i in range(r1+1, r2):
        for j in range(c1, c2+1):
            ii = int((i - (r1+1)) * sh2 / (r2 - r1 - 1) + 0.5)
            jj = int((j - c1) * sw2 / tw2 + 0.5)
            if 0 <= ii < sh2 and 0 <= jj < sw2 and grid[r4+ii][c4+jj] == c_small:
                out[i][j] = c_small
    return out