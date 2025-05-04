from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    rs = [r for r, _ in pts]
    cs = [c for _, c in pts]
    min_r, max_r = min(rs), max(rs)
    min_c, max_c = min(cs), max(cs)
    horiz = False
    if (min_r + max_r) % 2 == 0:
        rc = (min_r + max_r) // 2
        ok = True
        for r, c in pts:
            mr = 2 * rc - r
            if not (0 <= mr < h and grid[mr][c] == grid[r][c]):
                ok = False
                break
        horiz = ok
    vert = False
    if not horiz and (min_c + max_c) % 2 == 0:
        cc = (min_c + max_c) // 2
        ok = True
        for r, c in pts:
            mc = 2 * cc - c
            if not (0 <= mc < w and grid[r][mc] == grid[r][c]):
                ok = False
                break
        vert = ok
    out = [row[:] for row in grid]
    if horiz:
        for c in range(w):
            out[rc][c] = 3
    elif vert:
        for r in range(h):
            out[r][cc] = 3
    return out