import numpy as np

def solve(grid):
    g = np.array(grid)
    h, w = g.shape
    ys, xs = np.nonzero(g)
    vals = g[ys, xs]
    uniq, cnt = np.unique(vals[vals>0], return_counts=True)
    p = uniq[np.argsort(-cnt)][:2]
    mask = np.isin(g, p)
    comps = np.zeros_like(g, int)
    best_bb = None
    cid = 0
    for i in range(h):
        for j in range(w):
            if mask[i,j] and comps[i,j]==0:
                cid += 1
                stack = [(i,j)]
                comps[i,j] = cid
                bb = [i, i, j, j]
                while stack:
                    y, x = stack.pop()
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and mask[ny,nx] and comps[ny,nx]==0:
                            comps[ny,nx] = cid
                            stack.append((ny,nx))
                            bb = [min(bb[0],ny), max(bb[1],ny), min(bb[2],nx), max(bb[3],nx)]
                area = (bb[1]-bb[0])*(bb[3]-bb[2])
                if best_bb is None or area>best_bb[0]:
                    best_bb = (area, bb)
    _, (r0, r1, c0, c1) = best_bb
    P = g[r0:r1+1, c0:c1+1]
    ph, pw = P.shape
    out = g.copy()

    def fill_region(r0_, c0_, flipv, fliph, get_seeds):
        M = P.copy()
        if flipv: M = M[::-1]
        if fliph: M = M[:, ::-1]
        regs = (slice(r0_, r0_+ph), slice(c0_, c0_+pw))
        seeds = get_seeds()
        mp = {}
        for y0, x0 in seeds:
            v = g[y0, x0]
            py = y0 - r0_ if r0_<=y0<=r1 else (r1 - r0 if r0_<=r1<y0 else 0)
            px = x0 - c0_ if c0_<=x0<=c1 else (c1 - c0 if c0_<=c1<x0 else 0)
            pv = P[py, px]
            mp[pv] = v
        extras = [v for v in np.unique(g[regs]) if v>0 and v not in mp.values()]
        for pv in p:
            if pv not in mp:
                mp[pv] = extras.pop(0) if extras else 0
        wax = out[regs]
        for a in (p if len(p)==2 else mp):
            wax[M==a] = mp[a]

    def seeds_E():
        lst = [(y, x) for y in range(r0, r1+1) for x in range(c1+1, w) if g[y,x]>0]
        return sorted(lst, key=lambda t: (t[1], t[0]))[:2]

    def seeds_S():
        lst = [(y, x) for y in range(r1+1, h) for x in range(c0, c1+1) if g[y,x]>0]
        return sorted(lst, key=lambda t: (t[0], t[1]))[:2]

    def seeds_SE():
        lst = [(y, x) for y in range(r1+1, h) for x in range(c1+1, w) if g[y,x]>0]
        return sorted(lst, key=lambda t: (t[0]+t[1]))[:2]

    if c1+1<w:
        fill_region(r0, c1+1, False, True, seeds_E)
    if r1+1<h:
        fill_region(r1+1, c0, True, False, seeds_S)
    if r1+1<h and c1+1<w:
        fill_region(r1+1, c1+1, True, True, seeds_SE)

    return out.tolist()