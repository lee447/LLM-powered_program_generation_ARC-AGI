import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    A = np.array(grid)
    cnt = {}
    for v in A.flatten():
        cnt[v] = cnt.get(v, 0) + 1
    bg = max(cnt, key=cnt.get)
    rows = np.any(A != bg, axis=1).nonzero()[0]
    cols = np.any(A != bg, axis=0).nonzero()[0]
    top, bottom = rows[0], rows[-1]
    left, right = cols[0], cols[-1]
    size = bottom - top + 1
    bs = size // 3
    blocks = [[A[top + i*bs : top + (i+1)*bs, left + j*bs : left + (j+1)*bs].copy()
               for j in range(3)] for i in range(3)]
    def rot(b, k):
        return np.rot90(b, k, axes=(1,0))
    out = A.copy()
    b0 = top // bs + 1
    c0 = left // bs + 1
    for di, dj in [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]:
        br = b0 + 2*di
        bc = c0 + 2*dj
        if not (0 <= br < h//bs and 0 <= bc < w//bs):
            continue
        if di < 0:
            kr = 2
        elif di > 0:
            kr = 0
        else:
            kr = 1 if dj > 0 else 3
        sr = di + 1
        sc = dj + 1
        if di == 0:
            sc = 2 if dj > 0 else 0
        if dj == 0:
            sr = 0 if di < 0 else 2
        b = rot(blocks[sr][sc], kr)
        r0, c0p = br*bs, bc*bs
        out[r0:r0+bs, c0p:c0p+bs] = b
    return out.tolist()