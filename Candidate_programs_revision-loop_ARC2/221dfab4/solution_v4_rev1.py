import numpy as np

def solve(grid):
    arr = np.array(grid)
    h, w = arr.shape
    cnt = {c: int((arr==c).sum()) for c in np.unique(arr)}
    bg = max(cnt, key=lambda x: cnt[x])
    marker = [c for c in cnt if c not in (bg,) and cnt[c] < cnt.get(max(cnt, key=cnt.get),0)][0]
    thickness = 0
    for i in range(h):
        runs = np.diff(np.where(np.concatenate(([0],arr[i]==marker,[0])))[0])
        thickness = max(thickness, max(runs, default=0))
    shape = [c for c in cnt if c not in (bg,marker)][0]
    mask = arr==shape
    rows = np.where(mask.any(1))[0]
    cols = np.where(mask.any(0))[0]
    n, m = len(rows), len(cols)
    idxs_r = [0, n//4, n//2, 3*n//4]
    idxs_c = [m//4, m//2, 3*m//4]
    out = arr.copy()
    other = next(c for c in range(10) if c not in cnt)
    hcol = other
    vcol = marker
    for ir in idxs_r:
        r = rows[ir]
        for dt in range(thickness):
            rr = r + (0 if ir>0 else -thickness) + dt
            for j in cols:
                if mask[rr, j]:
                    out[rr, j] = hcol
    for ic in idxs_c:
        c = cols[ic]
        for dt in range(thickness):
            cc = c + dt
            for i in rows:
                if mask[i, cc]:
                    out[i, cc] = vcol
    return out.tolist()