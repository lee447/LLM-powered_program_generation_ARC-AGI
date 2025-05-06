import numpy as np
from collections import Counter

def solve(grid):
    g = np.array(grid)
    R, C = g.shape
    sep = 4
    cnt = Counter(g.flatten())
    newc = max((c for c in cnt if c not in (0,1,sep)), key=cnt.get)
    rows = [i for i in range(R) if (g[i]==sep).all()]
    cols = [j for j in range(C) if (g[:,j]==sep).all()]
    rb = []
    prev = -1
    for r in rows+[R]:
        if r-prev>1:
            rb.append((prev+1, r-1))
        prev = r
    cb = []
    prev = -1
    for c in cols+[C]:
        if c-prev>1:
            cb.append((prev+1, c-1))
        prev = c
    out = g.copy()
    for r0,r1 in rb:
        for c0,c1 in cb:
            block = g[r0:r1+1, c0:c1+1]
            h, w = block.shape
            ones = np.argwhere(block==1)
            if ones.size==0: continue
            if h==3 and w==3:
                if len(ones)==3:
                    ds = [np.linalg.norm(p-[1,1]) for p in ones]
                    ends = sorted(zip(ds,ones), reverse=True)[:2]
                    for _,(i,j) in ends:
                        out[r0+i, c0+j]=newc
                else:
                    pts = [(0,0),(0,2),(1,1)]
                    for i,j in pts:
                        if block[i,j]==1:
                            out[r0+i, c0+j]=newc
            else:
                midr = r0+(h-1)//2
                for j in (c0,c1):
                    if g[midr,j]==1:
                        out[midr,j]=newc
    return out.tolist()