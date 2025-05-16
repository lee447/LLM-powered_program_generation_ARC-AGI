from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = max(set(x for row in grid for x in row), key=lambda c: sum(r.count(c) for r in grid))
    cols = [c for c in set(x for row in grid for x in row) if c != bg]
    def bbox(color:int) -> Tuple[int,int,int,int]:
        rs = [i for i in range(h) for j in range(w) if grid[i][j]==color]
        cs = [j for i in range(h) for j in range(w) if grid[i][j]==color]
        return min(rs), min(cs), max(rs), max(cs)
    counts = {c: sum(row.count(c) for row in grid) for c in cols}
    ordered = sorted(cols, key=lambda c: counts[c])
    c_small, c_mid, c_large = ordered[0], ordered[1], ordered[2]
    r1,c1,r2,c2 = bbox(c_large)
    inner_h, inner_w = max(0, r2-r1-1), max(0, c2-c1-1)
    rm1, cm1, rm2, cm2 = bbox(c_mid)
    mh, mw = rm2-rm1+1, cm2-cm1+1
    newg = [row[:] for row in grid]
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if i==r1 or i==r2 or j==c1 or j==c2:
                newg[i][j] = c_large
            elif inner_h>0 and inner_w>0:
                rr = (i-(r1+1))*mh//inner_h
                cc = (j-(c1+1))*mw//inner_w
                if 0<=rm1+rr<h and 0<=cm1+cc<w and grid[rm1+rr][cm1+cc]==c_mid:
                    newg[i][j] = c_mid
                else:
                    newg[i][j] = bg
    return newg