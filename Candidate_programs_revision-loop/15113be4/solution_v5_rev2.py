import numpy as np
from collections import Counter

def solve(grid):
    g = np.array(grid)
    R, C = g.shape
    sep = next(c for c in Counter(g.flatten()) if any((g[i]==c).all() for i in range(R)))
    cnt = Counter(map(int, g.flatten()))
    newc = max((c for c in cnt if c not in (0,1,sep)), key=cnt.get)
    rows = [i for i in range(R) if (g[i]==sep).all()]
    cols = [j for j in range(C) if (g[:,j]==sep).all()]
    rb, cb = [], []
    p = -1
    for r in rows+[R]:
        if r-p>1: rb.append((p+1,r-1))
        p = r
    p = -1
    for c in cols+[C]:
        if c-p>1: cb.append((p+1,c-1))
        p = c
    out = g.copy()
    for r0,r1 in rb:
        for c0,c1 in cb:
            block = g[r0:r1+1, c0:c1+1]
            h, w = block.shape
            P = np.argwhere(block==1)
            if P.size==0: continue
            if h==3 and w==3:
                if len(P)==3:
                    for i,j in P:
                        out[r0+i, c0+j] = newc
                else:
                    rc = [int((block[i]==1).sum()) for i in range(3)]
                    if 3 in rc:
                        i = rc.index(3)
                        js = [j for j in range(3) if block[i,j]==1]
                        out[r0+i, c0+js[0]] = newc
                        out[r0+i, c0+js[-1]] = newc
            else:
                if h < w:
                    midr = r0 + h//2
                    for j in (c0, c1):
                        if g[midr,j]==1:
                            out[midr,j] = newc
                else:
                    midc = c0 + w//2
                    for i in (r0, r1):
                        if g[i,midc]==1:
                            out[i,midc] = newc
    return out.tolist()