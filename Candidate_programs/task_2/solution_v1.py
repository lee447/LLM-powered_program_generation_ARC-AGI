from typing import List, Tuple

def solve(grid: List[List[int]]) -> List[List[int]]:
    h0 = len(grid)
    w0 = len(grid[0]) if h0>0 else 0
    r0, r1 = h0, -1
    c0, c1 = w0, -1
    for i in range(h0):
        for j in range(w0):
            if grid[i][j] == 8:
                if i < r0: r0 = i
                if i > r1: r1 = i
                if j < c0: c0 = j
                if j > c1: c1 = j
    h = r1 - r0 + 1
    w = c1 - c0 + 1
    freq = {}
    mats = {}
    for i in range(h0 - h + 1):
        for j in range(w0 - w + 1):
            ok = True
            key = []
            for di in range(h):
                row = grid[i+di][j:j+w]
                if 8 in row:
                    ok = False
                    break
                key.append(tuple(row))
            if not ok:
                continue
            k = tuple(key)
            freq[k] = freq.get(k, 0) + 1
            if k not in mats:
                mats[k] = [list(r) for r in key]
    best = max(freq.items(), key=lambda x: (x[1], x[0]))[0]
    return mats[best]