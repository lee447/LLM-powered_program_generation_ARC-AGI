import numpy as np

def solve(grid):
    arr = np.array(grid)
    mask = (arr == 8)
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    r1, r2 = np.where(rows)[0][[0, -1]]
    c1, c2 = np.where(cols)[0][[0, -1]]
    h, w = r2 - r1 + 1, c2 - c1 + 1
    candidates = []
    n, m = arr.shape
    for dr, dc in [(-h, 0), (h, 0), (0, -w), (0, w)]:
        rr, cc = r1 + dr, c1 + dc
        if rr >= 0 and cc >= 0 and rr + h <= n and cc + w <= m:
            block = arr[rr:rr+h, cc:cc+w]
            if not np.any(block == 8):
                candidates.append(block)
    return candidates[0].tolist()