from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [[0]*w for _ in range(h)]
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
    if not pts:
        return out
    for r, c in pts:
        out[r][c] = 8
    rs = [r for r, _ in pts]
    cs = [c for _, c in pts]
    minr, maxr = min(rs), max(rs)
    minc, maxc = min(cs), max(cs)
    cr, cc = (minr + maxr)//2, (minc + maxc)//2
    tasks = deque([
        (minr, cc, -1, 0, 1),
        (maxr, cc, 1, 0, 1),
        (cr, minc, 0, -1, 1),
        (cr, maxc, 0, 1, 1),
    ])
    seen = set()
    while tasks:
        r0, c0, dr, dc, phase = tasks.popleft()
        key = (r0, c0, dr, dc, phase)
        if key in seen:
            continue
        seen.add(key)
        k = 1
        while True:
            r, c = r0 + dr*k, c0 + dc*k
            if not (0 <= r < h and 0 <= c < w):
                break
            if (phase == 1 and k % 2 == 1) or (phase == -1 and k % 2 == 0):
                if out[r][c] == 0:
                    out[r][c] = 8
                    tasks.append((r, c, dc, dr, -phase))
                    tasks.append((r, c, -dc, -dr, -phase))
            k += 1
    return out