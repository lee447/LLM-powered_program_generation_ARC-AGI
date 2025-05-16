import numpy as np

def solve(grid):
    g = np.array(grid)
    marker = 8
    ys, xs = np.where(g == marker)
    r0, r1 = ys.min(), ys.max()
    c0, c1 = xs.min(), xs.max()
    h, w = r1 - r0 + 1, c1 - c0 + 1
    R, C = g.shape
    def valid(sub):
        return np.all(sub != marker)
    if r0 >= h:
        up = g[r0-h:r0, c0:c0+w]
        if up.shape == (h, w) and valid(up):
            return up.tolist()
    if r1 + h < R:
        dn = g[r1+1:r1+1+h, c0:c0+w]
        if dn.shape == (h, w) and valid(dn):
            return dn.tolist()
    if c0 >= w:
        lt = g[r0:r0+h, c0-w:c0]
        if lt.shape == (h, w) and valid(lt):
            return lt.tolist()
    if c1 + w < C:
        rt = g[r0:r0+h, c1+1:c1+1+w]
        if rt.shape == (h, w) and valid(rt):
            return rt.tolist()
    return []