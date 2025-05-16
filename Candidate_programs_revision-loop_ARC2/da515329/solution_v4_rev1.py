import numpy as np

def solve(grid):
    a = np.array(grid)
    ys, xs = np.where(a == 8)
    r0, r1 = ys.min(), ys.max()
    c0, c1 = xs.min(), xs.max()
    H, W = r1 - r0 + 1, c1 - c0 + 1
    r = (H - 1) // 2
    c = (W - 1) // 2
    T = H + 1
    out = np.zeros_like(a)
    oy, ox = r0 + r, c0 + c
    for y in range(a.shape[0]):
        dy = (y - oy) % T - r
        for x in range(a.shape[1]):
            dx = (x - ox) % T - c
            if abs(dy) + abs(dx) == r + 1 and (dy == 0 or dx == 0):
                out[y, x] = 8
    return out.tolist()