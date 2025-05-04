from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != 0]
    rs = [r for r, _ in pts]
    cs = [c for _, c in pts]
    min_r, max_r = min(rs), max(rs)
    min_c, max_c = min(cs), max(cs)
    sum_r = min_r + max_r
    if sum_r % 2 == 0:
        axis_r = sum_r // 2
        axis_rows = {axis_r}
    else:
        r0 = sum_r // 2
        axis_rows = {r0, r0 + 1}
        axis_r = r0 + 1
    ok_h = True
    for r in range(min_r, max_r + 1):
        mr = sum_r - r
        for c in range(min_c, max_c + 1):
            if r in axis_rows or mr in axis_rows:
                continue
            if grid[r][c] != grid[mr][c]:
                ok_h = False
                break
        if not ok_h:
            break
    sum_c = min_c + max_c
    if sum_c % 2 == 0:
        axis_c = sum_c // 2
        axis_cols = {axis_c}
    else:
        c0 = sum_c // 2
        axis_cols = {c0, c0 + 1}
        axis_c = c0 + 1
    ok_v = True
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            mc = sum_c - c
            if c in axis_cols or mc in axis_cols:
                continue
            if grid[r][c] != grid[r][mc]:
                ok_v = False
                break
        if not ok_v:
            break
    out = [row[:] for row in grid]
    if ok_h and all(grid[axis_r][c] == 0 for c in range(w)):
        for c in range(w):
            out[axis_r][c] = 3
    elif ok_v and all(grid[r][axis_c] == 0 for r in range(h)):
        for r in range(h):
            out[r][axis_c] = 3
    return out