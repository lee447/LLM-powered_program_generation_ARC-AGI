import numpy as np

def solve(grid):
    g = np.array(grid)
    R, C = g.shape
    blue = np.argwhere(g == 1)
    rows = set(blue[:,0])
    nonb = np.argwhere((g != 0) & (g != 1))
    inside = [tuple(x) for x in nonb if x[0] in rows]
    outside = [tuple(x) for x in nonb if x[0] not in rows]
    if not outside:
        outside = inside
    piv_r, piv_c = None, None
    cnt = {}
    for r, c in blue:
        cnt[r] = cnt.get(r, 0) + 1
    pr = min(cnt, key=lambda r: cnt[r])
    pcs = [c for r, c in blue if r == pr]
    pc = pcs[0]
    ar1, ac1 = inside[0]
    ar2, ac2 = outside[0]
    rel = [(r - pr, c - pc) for r, c in blue]
    out = g.copy()
    v1 = g[ar1, ac1]
    v2 = g[ar2, ac2]
    for dr, dc in rel:
        nr, nc = ar1 + dr, ac1 - dc
        if 0 <= nr < R and 0 <= nc < C:
            out[nr, nc] = v1
    for dr, dc in rel:
        nr, nc = ar2 - dr, ac2 + dc
        if 0 <= nr < R and 0 <= nc < C:
            out[nr, nc] = v2
    return out.tolist()