from typing import List
import itertools
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cnt = {}
    for row in grid:
        for c in row:
            cnt[c] = cnt.get(c, 0) + 1
    bg = max(cnt, key=lambda k: cnt[k])
    colors = [c for c in cnt if c != bg]
    pos = {c: [] for c in colors}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c in pos:
                pos[c].append((i, j))
    best_n = -1
    c1 = None
    p1 = p2 = None
    for c in colors:
        pts = pos[c]
        for a, b in itertools.combinations(pts, 2):
            dr = b[0] - a[0]
            dc = b[1] - a[1]
            if abs(dr) == abs(dc) and abs(dr) > best_n:
                best_n = abs(dr)
                c1 = c
                p1, p2 = a, b
    if c1 is None:
        return [row[:] for row in grid]
    def sgn(x):
        return (x > 0) - (x < 0)
    dr = sgn(p2[0] - p1[0])
    dc = sgn(p2[1] - p1[1])
    c2 = next((c for c in colors if c != c1), None)
    out = [row[:] for row in grid]
    for t in range(best_n + 1):
        r = p1[0] + dr * t
        c = p1[1] + dc * t
        if out[r][c] != c2:
            out[r][c] = c1
    if c2 is not None:
        for (r0, c0) in pos[c2]:
            if (r0 - p1[0]) * dc == (c0 - p1[1]) * dr:
                dr2, dc2 = -dc, dr
                r, c = r0, c0
                while 0 <= r < h and 0 <= c < w:
                    if out[r][c] == bg:
                        out[r][c] = c2
                    r += dr2; c += dc2
                r, c = r0 - dr2, c0 - dc2
                while 0 <= r < h and 0 <= c < w:
                    if out[r][c] == bg:
                        out[r][c] = c2
                    r -= dr2; c -= dc2
    return out