import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    pts = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != bg:
                pts.setdefault(c, []).append((i,j))
    cols = sorted(pts.keys(), key=lambda c: len(pts[c]), reverse=True)
    colA, colB = cols[0], cols[-1]
    A = pts[colA]
    B = pts[colB]
    def center(pts):
        rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
        return ((min(rs)+max(rs))//2, (min(cs)+max(cs))//2)
    cA = center(A)
    cB = center(B)
    offsA = [(r-cA[0], c-cA[1]) for r,c in A]
    offsB = [(r-cB[0], c-cB[1]) for r,c in B]
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