import numpy as np
def solve(grid):
    arr = np.array(grid)
    h, w = arr.shape
    mask = ((arr==9) | (arr==4)).astype(float)
    rd = np.sum(mask, axis=1)/w
    cd = np.sum(mask, axis=0)/h
    # choose threshold based on overall density; use 0.2 as a heuristic
    thr = 0.2
    # pick central row and col as the ones with maximum density
    r_center = int(np.argmax(rd))
    c_center = int(np.argmax(cd))
    r0 = r_center
    while r0 > 0 and rd[r0-1] >= thr:
        r0 -= 1
    r1 = r_center
    while r1 < h-1 and rd[r1+1] >= thr:
        r1 += 1
    c0 = c_center
    while c0 > 0 and cd[c0-1] >= thr:
        c0 -= 1
    c1 = c_center
    while c1 < w-1 and cd[c1+1] >= thr:
        c1 += 1
    sub = arr[r0:r1+1, c0:c1+1]
    return sub.tolist()