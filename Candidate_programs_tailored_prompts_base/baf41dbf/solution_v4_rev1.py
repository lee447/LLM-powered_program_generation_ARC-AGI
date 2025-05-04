from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    orig_rs = []
    orig_cs = []
    pinks = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 3:
                orig_rs.append(r)
                orig_cs.append(c)
            elif grid[r][c] == 6:
                pinks.append((r, c))
    top = min(orig_rs)
    bottom = max(orig_rs)
    left = min(orig_cs)
    right = max(orig_cs)
    new_top, new_bottom, new_left, new_right = top, bottom, left, right
    for r, c in pinks:
        if top <= r <= bottom:
            if c < left:
                new_left = c + 1
            elif c > right:
                new_right = c - 1
        if left <= c <= right:
            if r < top:
                new_top = r + 1
            elif r > bottom:
                new_bottom = r - 1
    interior = []
    for c in range(left + 1, right):
        ok = True
        for r in range(top, bottom + 1):
            if grid[r][c] != 3:
                ok = False
                break
        if ok:
            interior.append(c)
    if interior:
        interior.sort()
        mid = interior[len(interior) // 2]
    out = [[0] * w for _ in range(h)]
    for c in range(new_left, new_right + 1):
        out[new_top][c] = 3
        out[new_bottom][c] = 3
    for r in range(new_top, new_bottom + 1):
        out[r][new_left] = 3
        out[r][new_right] = 3
    if interior:
        for r in range(new_top, new_bottom + 1):
            out[r][mid] = 3
    for r, c in pinks:
        out[r][c] = 6
    return out