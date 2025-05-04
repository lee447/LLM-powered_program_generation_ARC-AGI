from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    prefix = []
    for x in range(w):
        if grid[0][x] == 0:
            break
        prefix.append(grid[0][x])
    dpos = None
    dot = None
    for x in range(len(prefix), w):
        if grid[0][x] != 0:
            dpos = x
            dot = grid[0][x]
            break
    out = [row[:] for row in grid]
    if dpos is not None:
        out[0][dpos] = grid[1][dpos]
    ar = ac = None
    for r in range(2, h):
        for c in range(w):
            if grid[r][c] != 0:
                ar, ac = r, c
                break
        if ar is not None:
            break
    p = len(prefix)
    R = p - 1 if dot is None else p + 1
    for r in range(R, 0, -1):
        if r == R and dot is not None:
            col = dot
        elif r <= p - 1:
            col = prefix[r]
        else:
            continue
        r0, r1 = ar - r, ar + r
        c0, c1 = ac - r, ac + r
        if 0 <= r0 < h:
            for x in range(c0, c1 + 1):
                if 0 <= x < w:
                    out[r0][x] = col
        if 0 <= r1 < h:
            for x in range(c0, c1 + 1):
                if 0 <= x < w:
                    out[r1][x] = col
        for y in range(r0, r1 + 1):
            if 0 <= y < h:
                if 0 <= c0 < w:
                    out[y][c0] = col
                if 0 <= c1 < w:
                    out[y][c1] = col
    return out