import numpy as np
from collections import defaultdict

def solve(grid):
    h, w = len(grid), len(grid[0])
    rows = [i for i in range(h) if all(grid[i][j] == 4 for j in range(w))]
    cols = [j for j in range(w) if all(grid[i][j] == 4 for i in range(h))]
    r_segs = []
    prev = -1
    for r in rows + [h]:
        if r - prev > 1:
            r_segs.append((prev + 1, r))
        prev = r
    c_segs = []
    prev = -1
    for c in cols + [w]:
        if c - prev > 1:
            c_segs.append((prev + 1, c))
        prev = c
    br = len(r_segs)
    bc = len(c_segs)
    accent = None
    for i in range(h):
        for j in range(w):
            if grid[i][j] not in (0,1,4):
                accent = grid[i][j]
                break
        if accent is not None:
            break
    have = {}
    for bi in range(br):
        rs, re = r_segs[bi]
        for bj in range(bc):
            cs, ce = c_segs[bj]
            found = [(i - rs, j - cs) for i in range(rs, re) for j in range(cs, ce) if grid[i][j] == accent]
            if found:
                have[(bi, bj)] = found
    (br0, bj0), pts0 = next(iter(have.items()))
    rs0, re0 = r_segs[br0]
    cs0, ce0 = c_segs[bj0]
    bw = c_segs[bj0][1] - c_segs[bj0][0]
    D = defaultdict(list)
    for r0, c0 in pts0:
        D[r0].append(c0)
    out = [row[:] for row in grid]
    for bj in range(bc):
        if (br0, bj) in have: continue
        cs, ce = c_segs[bj]
        wj = ce - cs
        for r0, cols0 in D.items():
            for c0 in cols0:
                c_small = (c0 + (bj - bj0)) % bw
                if c_small < wj:
                    out[rs0 + r0][cs + c_small] = accent
    return out