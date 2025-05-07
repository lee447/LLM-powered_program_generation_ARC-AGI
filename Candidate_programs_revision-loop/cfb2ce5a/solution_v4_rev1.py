import numpy as np

def solve(grid):
    g = np.array(grid)
    h, w = g.shape
    ys, xs = np.nonzero(g)
    vals = g[ys, xs]
    uniq, cnt = np.unique(vals[vals>0], return_counts=True)
    p = uniq[np.argsort(-cnt)][:2]
    p0, p1 = min(p), max(p)
    mask = np.isin(g, p)
    comps, num = np.zeros_like(g), 0
    bbest = None
    for i in range(h):
        for j in range(w):
            if mask[i,j] and comps[i,j]==0:
                num+=1
                stack = [(i,j)]
                comps[i,j]=num
                bb = [i,i,j,j]
                while stack:
                    y,x = stack.pop()
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx = y+dy,x+dx
                        if 0<=ny<h and 0<=nx<w and mask[ny,nx] and comps[ny,nx]==0:
                            comps[ny,nx]=num
                            stack.append((ny,nx))
                            bb = [min(bb[0],ny), max(bb[1],ny), min(bb[2],nx), max(bb[3],nx)]
                area = (bb[1]-bb[0])*(bb[3]-bb[2])
                if bbest is None or area>bbest[0]:
                    bbest = (area, bb)
    _, (r0,r1,c0,c1) = bbest
    P = g[r0:r1+1, c0:c1+1]
    ph, pw = P.shape
    out = g.copy()
    def copy_quad(r0_, c0_, A, seeds, flipv, fliph):
        if len(seeds)==0: return
        if len(seeds)==1:
            out[r0_:r0_+ph, c0_:c0_+pw] = seeds[0]
            return
        s0, s1 = seeds
        M = A.copy()
        if flipv: M = M[::-1]
        if fliph: M = M[:, ::-1]
        mask0 = (M==p0)
        out[r0_:r0_+ph, c0_:c0_+pw][mask0] = s0
        out[r0_:r0_+ph, c0_:c0_+pw][~mask0] = s1

    seeds = []
    for y,x in zip(ys, xs):
        if y<=r1 and x>c1: seeds.append((y,x,g[y,x]))
    seeds = sorted(seeds, key=lambda z: z[0])
    s1 = seeds[0][2] if len(seeds)>0 else None
    s2 = seeds[-1][2] if len(seeds)>1 else None
    copy_quad(r0, c1+1, P, [s2, s1] if s1 and s2 else [s1 or s2], False, True)

    seeds = []
    for y,x in zip(ys, xs):
        if y>r1 and x<=c0: seeds.append((y,x,g[y,x]))
    seeds = sorted(seeds, key=lambda z: z[0])
    s1 = seeds[0][2] if len(seeds)>0 else None
    s2 = seeds[-1][2] if len(seeds)>1 else None
    copy_quad(r1+1, c0, P, [s1, s2] if s1 and s2 else [s1 or s2], True, False)

    seeds = []
    for y,x in zip(ys, xs):
        if y>r1 and x>c1: seeds.append((y,x,g[y,x]))
    seeds = sorted(seeds, key=lambda z: z[0])
    s1 = seeds[0][2] if len(seeds)>0 else None
    s2 = seeds[-1][2] if len(seeds)>1 else None
    copy_quad(r1+1, c1+1, P, [s2, s1] if s1 and s2 else [s1 or s2], True, True)

    return out.tolist()