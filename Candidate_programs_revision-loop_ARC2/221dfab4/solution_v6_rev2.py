import numpy as np

def solve(grid):
    arr = np.array(grid)
    h, w = arr.shape
    cnt = {c: int((arr == c).sum()) for c in np.unique(arr)}
    bg = max(cnt, key=cnt.get)
    others = sorted((c for c in cnt if c != bg), key=lambda c: cnt[c])
    marker = others[0]
    shape = others[-1]
    rm, cm = np.where(arr == marker)
    mh = rm.max() - rm.min() + 1
    mw = cm.max() - cm.min() + 1
    mask = arr == shape
    rows = np.where(mask.any(1))[0]
    cols = np.where(mask.any(0))[0]
    n, m = len(rows), len(cols)
    idxs_r = [0, n//4, n//2, 3*n//4]
    idxs_c = [m//4, m//2, 3*m//4]
    out = arr.copy()
    hcol = next(c for c in range(10) if c not in (bg, marker, shape))
    vcol = marker
    for ir in idxs_r:
        base = rows[ir] - (mh if ir == 0 else 0)
        for dt in range(mh):
            rr = base + dt
            if 0 <= rr < h:
                for j in cols:
                    if mask[rr, j]:
                        out[rr, j] = hcol
    for ic in idxs_c:
        base = cols[ic]
        for dt in range(mw):
            cc = base + dt
            if 0 <= cc < w:
                for i in rows:
                    if mask[i, cc]:
                        out[i, cc] = vcol
    return out.tolist()