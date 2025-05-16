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
    rB = np.any(B != 0, axis=1).sum()
    cA = np.any(A != 0, axis=0).sum()
    full_v = rB // h
    full_h = cA // w
    rem_v = rB % h
    rem_h = cA % w
    if rB == 0 and cA == 0:
        return E.tolist()
    rows = full_v * h + rem_v
    cols = full_h * w + rem_h
    repv = full_v + (1 if rem_v else 0)
    reph = full_h + (1 if rem_h else 0)
    out = np.tile(E, (repv, reph))
    return out[:rows, :cols].tolist()