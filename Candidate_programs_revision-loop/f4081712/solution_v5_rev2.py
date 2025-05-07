import numpy as np
from typing import List
from collections import Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    arr = np.array(grid)
    H, W = arr.shape
    ys, xs = np.where(arr == 3)
    rmin, rmax = ys.min(), ys.max()
    cmin, cmax = xs.min(), xs.max()
    h, w = rmax - rmin + 1, cmax - cmin + 1
    x0, y0 = rmin % h, cmin % w
    cnt = Counter()
    pos = {}
    for i in range(x0, H - h + 1, h):
        for j in range(y0, W - w + 1, w):
            block = arr[i:i+h, j:j+w]
            if np.any(block == 3): continue
            key = tuple(block.flatten())
            cnt[key] += 1
            pos.setdefault(key, []).append((i, j))
    if not cnt:
        return [[0]*w for _ in range(h)]
    best_count = max(cnt.values())
    candidates = [k for k, v in cnt.items() if v == best_count]
    best_key = min(candidates, key=lambda k: min(abs(i - rmin) + abs(j - cmin) for i, j in pos[k]))
    blk = np.array(best_key).reshape(h, w)
    return blk.tolist()