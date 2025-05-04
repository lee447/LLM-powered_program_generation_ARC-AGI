import numpy as np
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0]) if grid else (0, 0)
    g = np.array(grid)
    out = g.copy()
    # find sentinel
    pos2 = np.argwhere(g == 2)
    if pos2.shape[0]:
        sr, sc = pos2[0]
    else:
        sr = sc = None
    # find vertical triple centers
    vcenters = []
    for c in range(w):
        for r in range(h-2):
            v = g[r, c]
            if v != 0 and g[r+1, c] == v and g[r+2, c] == v and (r == 0 or g[r-1, c] != v):
                vcenters.append((r+1, c))
    # find horizontal triple centers
    hcenters = []
    for r in range(h):
        for c in range(w-2):
            v = g[r, c]
            if v != 0 and g[r, c+1] == v and g[r, c+2] == v and (c == 0 or g[r, c-1] != v):
                hcenters.append((r, c+1))
    # connect vertical centers on same row
    rows = {}
    for r, c in vcenters:
        rows.setdefault(r, []).append(c)
    for r, cols in rows.items():
        cols = sorted(set(cols))
        for i in range(len(cols)-1):
            c1, c2 = cols[i], cols[i+1]
            for cc in range(c1+1, c2):
                if out[r, cc] == 0 and g[r, cc-1] == 0:
                    out[r, cc] = 2
    # connect horizontal centers on same col
    cols = {}
    for r, c in hcenters:
        cols.setdefault(c, []).append(r)
    for c, rows_ in cols.items():
        rows_ = sorted(set(rows_))
        for i in range(len(rows_)-1):
            r1, r2 = rows_[i], rows_[i+1]
            for rr in range(r1+1, r2):
                if out[rr, c] == 0 and g[rr-1, c] == 0:
                    out[rr, c] = 2
    # connect sentinel to first vertical center
    if sr is not None and vcenters:
        vc = sorted(vcenters, key=lambda x: abs(x[1]-sc))[0]
        r0, c0 = sr, sc
        r1, c1 = vc
        # vertical then horizontal
        dr = 1 if r1 > r0 else -1
        for rr in range(r0+dr, r1, dr):
            if out[rr, c0] == 0:
                out[rr, c0] = 2
        dc = 1 if c1 > c0 else -1
        row = r1
        for cc in range(c0+dc, c1, dc):
            if out[row, cc] == 0:
                out[row, cc] = 2
    return out.tolist()