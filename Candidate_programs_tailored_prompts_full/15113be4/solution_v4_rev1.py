import numpy as np

def solve(grid):
    g = np.array(grid)
    grey = 4
    rows = np.all(g==grey,axis=1)
    cols = np.all(g==grey,axis=0)
    r_idx = np.where(~rows)[0]
    c_idx = np.where(~cols)[0]
    dr = np.diff(np.concatenate(([-1],np.where(rows)[0],([g.shape[0]])))[[0,1]])
    dc = np.diff(np.concatenate(([-1],np.where(cols)[0],([g.shape[1]])))[[0,1]])
    rr = np.split(r_idx,np.cumsum(dr[:-1]))[:-1]
    cc = np.split(c_idx,np.cumsum(dc[:-1]))[:-1]
    blocks = {(i,j):g[np.ix_(rr[i],cc[j])] for i in range(len(rr)) for j in range(len(cc))}
    ac = next(v for v in np.unique(g) if v not in (0,1,grey))
    orig = [(i,j) for (i,j),b in blocks.items() if ac in b]
    base = blocks[orig[0]]
    out = g.copy()
    for bi in range(len(rr)):
        for bj in range(len(cc)):
            if (bi,bj) in orig: continue
            B = blocks[(bi,bj)]
            if B.shape!=base.shape: continue
            mask = base==ac
            block = out[np.ix_(rr[bi],cc[bj])]
            block[mask] = ac
            out[np.ix_(rr[bi],cc[bj])] = block
    return out.tolist()