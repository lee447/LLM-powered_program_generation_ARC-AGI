from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cutc = next(j for j in range(w) if any(grid[i][j] == 4 for i in range(h)))
    out = [[0] * cutc for _ in range(h)]
    left_nonzero = [any(grid[i][j] != 0 for j in range(cutc)) for i in range(h)]
    blocks = []
    i = 0
    while i < h:
        if left_nonzero[i]:
            j = i
            while j < h and left_nonzero[j]:
                j += 1
            blocks.append((i, j))
            i = j
        else:
            i += 1
    for i in range(h):
        for j in range(cutc + 1, w):
            v = grid[i][j]
            if v != 0 and v != 4:
                oj = j - cutc - 1
                if 0 <= oj < cutc:
                    out[i][oj] = v
    for rs, re in blocks:
        cols = {}
        for i in range(rs, re):
            for j in range(cutc):
                v = grid[i][j]
                if v != 0:
                    cols.setdefault(v, []).append((i, j))
        if not cols:
            continue
        best = None
        bestx = w
        for c, pts in cols.items():
            mx = min(p[1] for p in pts)
            if mx < bestx:
                bestx = mx
                best = c
        pts = cols[best]
        miny = min(p[0] for p in pts)
        minx = min(p[1] for p in pts)
        for i, j in pts:
            oi = rs + (i - miny)
            oj = j - minx
            if 0 <= oi < h and 0 <= oj < cutc:
                out[oi][oj] = best
    return out