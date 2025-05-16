from typing import List
from collections import Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cnt = Counter(x for row in grid for x in row)
    bg = cnt.most_common(1)[0][0]
    cx, cy = (w - 1) / 2, (h - 1) / 2

    def rot_ccw(r, c):
        dx, dy = c - cx, r - cy
        dx2, dy2 = -dy, dx
        return int(round(cy + dy2)), int(round(cx + dx2))

    # rotate
    tmp = [[bg] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != bg:
                nr, nc = rot_ccw(r, c)
                tmp[nr][nc] = v

    # shift so that topmost non-bg row is 0
    minr = min(r for r in range(h) for c in range(w) if tmp[r][c] != bg)
    out = [[bg] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            v = tmp[r][c]
            if v != bg:
                rr = r - minr
                out[rr][c] = v
    return out