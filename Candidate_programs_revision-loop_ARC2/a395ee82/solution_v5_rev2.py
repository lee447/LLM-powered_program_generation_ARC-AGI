import numpy as np
def solve(grid):
    h, w = len(grid), len(grid[0])
    vals = {}
    for i in range(h):
        for j in range(w):
            vals.setdefault(grid[i][j], []).append((i,j))
    bg = max(vals.keys(), key=lambda c: len(vals[c]))
    colors = [c for c in vals if c != bg]
    pts = {c: vals[c] for c in colors}
    bbs = {}
    for c,p in pts.items():
        rs = [x for x,y in p]; cs = [y for x,y in p]
        bbs[c] = (min(rs), max(rs), min(cs), max(cs))
    areas = {c: (bbs[c][1]-bbs[c][0]+1)*(bbs[c][3]-bbs[c][2]+1) for c in pts}
    colA, colB = sorted(areas, key=areas.get)
    minrA, maxrA, mincA, maxcA = bbs[colA]
    minrB, maxrB, mincB, maxcB = bbs[colB]
    cA = ((minrA+maxrA)//2, (mincA+maxcA)//2)
    cB = ((minrB+maxrB)//2, (mincB+maxcB)//2)
    offsA = [(r-cA[0], c-cA[1]) for r,c in pts[colA]]
    offsB = [(r-cB[0], c-cB[1]) for r,c in pts[colB]]
    out = [[bg]*w for _ in range(h)]
    for dr,dc in offsA:
        r, c = cB[0]+dr, cB[1]+dc
        if 0 <= r < h and 0 <= c < w:
            out[r][c] = colA
    for dr,dc in offsB:
        r, c = cA[0]+dr, cA[1]+dc
        if 0 <= r < h and 0 <= c < w:
            out[r][c] = colB
    return out