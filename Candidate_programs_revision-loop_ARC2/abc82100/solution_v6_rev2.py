from typing import List
from collections import defaultdict

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    coords = defaultdict(list)
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c:
                coords[c].append((i, j))
    hor = ver = None
    for c, pts in coords.items():
        rows = {i for i, _ in pts}
        cols = {j for _, j in pts}
        if len(rows) == 1 and len(pts) > 1:
            i = next(iter(rows))
            js = [j for _, j in pts]
            hor = (i, min(js), len(js), c)
        if len(cols) == 1 and len(pts) > 1:
            j = next(iter(cols))
            is_ = [i for i, _ in pts]
            ver = (min(is_), j, len(is_), c)
    out = [[0] * w for _ in range(h)]
    if hor and ver:
        ri, cj, Lh, ch = hor
        ci, rj, Lv, cv = ver
        for x in range(Lh):
            out[ri][cj + x] = cv
        for y in range(Lv):
            out[ci + y][rj] = ch
    return out