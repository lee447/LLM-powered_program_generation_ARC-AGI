from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    from collections import defaultdict, deque
    cols = set(v for row in grid for v in row if v != 0)
    best = None
    for c in cols:
        minr, maxr, minc, maxc = h, -1, w, -1
        for i in range(h):
            for j in range(w):
                if grid[i][j] == c:
                    minr = min(minr, i); maxr = max(maxr, i)
                    minc = min(minc, j); maxc = max(maxc, j)
        H = maxr - minr + 1
        W = maxc - minc + 1
        if H >= 3 and W >= 3:
            ok = True
            for i in range(minr, maxr+1):
                for j in range(minc, maxc+1):
                    border = (i==minr or i==maxr or j==minc or j==maxc)
                    if border:
                        if grid[i][j] != c: ok = False
                    else:
                        if grid[i][j] != 0: ok = False
            if ok:
                area = H*W
                if best is None or area < best[0]:
                    best = (area, c, minr, maxr, minc, maxc)
    if best is None:
        return [[]]
    _, C, minr, maxr, minc, maxc = best
    H, W = maxr-minr+1, maxc-minc+1
    res = [[C if (i==0 or i==H-1 or j==0 or j==W-1) else 0 for j in range(W)] for i in range(H)]
    return res