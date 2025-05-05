import numpy as np
def solve(grid):
    g = np.array(grid)
    n, m = g.shape
    rows = [i for i in range(n) if np.count_nonzero(g[i]==4)>m//2]
    cols = [j for j in range(m) if np.count_nonzero(g[:,j]==4)>n//2]
    rows = [-1]+rows+[n]
    cols = [-1]+cols+[m]
    regions = []
    for i in range(len(rows)-1):
        r0,r1 = rows[i]+1, rows[i+1]-1
        if r0<=r1:
            for j in range(len(cols)-1):
                c0,c1 = cols[j]+1, cols[j+1]-1
                if c0<=c1:
                    regions.append((r0,r1,c0,c1))
    for r0,r1,c0,c1 in regions:
        block = g[r0:r1+1,c0:c1+1]
        vals = np.unique(block[(block!=0)&(block!=1)&(block!=4)])
        if vals.size!=1: continue
        c = int(vals[0])
        pts = np.argwhere(block==c)
        if pts.shape[0]!=4: continue
        for a in range(4):
            for b in range(a+1,4):
                dr = pts[b,0]-pts[a,0]
                dc = pts[b,1]-pts[a,1]
                if dr*dc>0:
                    ep = [pts[a],pts[b]]
                    break
            else: continue
            break
        if not ep: continue
        center = np.array([(r1-r0)/2,(c1-c0)/2])
        for p in ep:
            nr = int(r0 + (r1-r0) - p[0])
            nc = int(c0 + (c1-c0) - p[1])
            if r0<=nr<=r1 and c0<=nc<=c1 and g[nr,nc]==1:
                g[nr,nc]=c
    return g.tolist()