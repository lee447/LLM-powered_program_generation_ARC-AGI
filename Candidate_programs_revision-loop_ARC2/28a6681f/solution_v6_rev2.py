import numpy as np
from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    g = np.array(grid)
    h, w = g.shape
    import itertools
    def find_rods(c):
        hrod = vrod = None
        for r in range(h):
            runs = [sum(1 for _ in grp) for val, grp in itertools.groupby(g[r]==c) if val]
            if runs and max(runs) >= 3:
                # find that run's columns
                row = g[r]
                cur = 0
                for i in range(w):
                    if row[i]==c:
                        cur+=1
                        if cur==max(runs):
                            hrod = (r, i-max(runs)+1, i)
                            break
                    else:
                        cur=0
                break
        for col in range(w):
            runs = [sum(1 for _ in grp) for val, grp in itertools.groupby(g[:,col]==c) if val]
            if runs and max(runs) >= 3:
                cur = 0
                for i in range(h):
                    if g[i,col]==c:
                        cur+=1
                        if cur==max(runs):
                            vrod = (col, i-max(runs)+1, i)
                            break
                    else:
                        cur=0
                break
        return hrod, vrod

    rods = []
    for c in np.unique(g):
        if c==0: continue
        hrod, vrod = find_rods(c)
        if hrod is not None and vrod is not None:
            rods.append((c, hrod, vrod))
    # pick the one whose horizontal rod is lowest; tie -> larger vertical length
    best = None
    for c, (r, cs, ce), (cc, rs, re) in rods:
        score = (r, re-rs)
        if best is None or score>best[0]:
            best = (score, c, r, cs, ce, rs, re)
    if best is None:
        return grid
    _, c, hr, c0, c1, r0, r1 = best
    rect_r0, rect_r1 = min(r0, hr), max(r1, hr)
    rect_c0, rect_c1 = min(c0, cc), max(c1, cc)
    # fill interior of the L (inside the rectangle but off the two arms)
    for rr in range(rect_r0+1, rect_r1):
        for cc2 in range(rect_c0+1, rect_c1):
            if g[rr, cc2] != 0 and g[rr, cc2] != c:
                g[rr, cc2] = 1
    return g.tolist()