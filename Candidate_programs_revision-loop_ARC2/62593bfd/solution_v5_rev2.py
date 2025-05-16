from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    from collections import Counter
    bg = Counter(c for row in grid for c in row).most_common(1)[0][0]
    cx, cy = (w - 1) / 2.0, (h - 1) / 2.0
    def rot_cw(r, c):
        dx, dy = c - cx, r - cy
        dx2, dy2 = dy, -dx
        return int(round(cy + dy2)), int(round(cx + dx2))
    tmp = [[bg] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != bg:
                nr, nc = rot_cw(r, c)
                tmp[nr][nc] = v
    minr = min(r for r in range(h) for c in range(w) if tmp[r][c] != bg)
    out = [[bg] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            v = tmp[r][c]
            if v != bg:
                out[r - minr][c] = v
    return out