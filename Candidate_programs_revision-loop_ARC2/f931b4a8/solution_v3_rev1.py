import numpy as np

def solve(grid):
    arr = np.array(grid)
    R, C = arr.shape
    h, w = R // 2, C // 2
    A = arr[:h, :w]
    B = arr[:h, w:]
    C3 = arr[h:, :w]
    D = arr[h:, w:]
    E = np.where(D == 0, C3, D)
    # count nonzero rows in the top-left quadrant
    nr = np.count_nonzero(np.any(A != 0, axis=1))
    # count nonzero cols in the top-right quadrant
    nc = np.count_nonzero(np.any(B != 0, axis=0))
    if np.all(D == 0):
        return E.tolist()
    H = 2 * nr
    W = 2 * nc
    repv = (H + h - 1) // h
    reph = (W + w - 1) // w
    out = np.tile(E, (repv, reph))
    return out[:H, :W].tolist()