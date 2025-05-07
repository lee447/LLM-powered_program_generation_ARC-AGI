from typing import List
from collections import Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    rmin, rmax, cmin, cmax = H, -1, W, -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 3:
                if i < rmin: rmin = i
                if i > rmax: rmax = i
                if j < cmin: cmin = j
                if j > cmax: cmax = j
    h, w = rmax - rmin + 1, cmax - cmin + 1
    cnt = Counter()
    for i in range(H - h + 1):
        for j in range(W - w + 1):
            flat = []
            ok = True
            for di in range(h):
                row = grid[i + di][j:j + w]
                if 3 in row:
                    ok = False
                    break
                flat.extend(row)
            if ok:
                cnt[tuple(flat)] += 1
    pat, _ = cnt.most_common(1)[0]
    out = [list(pat[i * w:(i + 1) * w]) for i in range(h)]
    return out