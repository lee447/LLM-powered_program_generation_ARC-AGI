from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = 8
    vert = {}
    for x in range(w):
        cnt = sum(1 for y in range(h) if grid[y][x] != bg)
        if cnt > 1:
            vert[x] = cnt
    xv = max(vert, key=vert.get)
    ys = [y for y in range(h) if grid[y][xv] != bg]
    y0, y1 = min(ys), max(ys)
    small = []
    for x in range(w):
        if x == xv: continue
        col = [y for y in range(h) if grid[y][x] != bg]
        if len(col) > 1:
            small.append((x, min(col), max(col), grid[col[0]][x]))
    if not small:
        return [row[:] for row in grid]
    centers = [(ym + yM) // 2 for x, ym, yM, c in small]
    lengths = [yM - ym + 1 for x, ym, yM, c in small]
    lst = list(zip(small, lengths, centers))
    lst.sort(key=lambda t: t[0][0])
    L = [l for _, l, _ in lst]
    NL = list(reversed(L))
    cy = (y0 + y1) // 2
    out = [row[:] for row in grid]
    for (x, ym, yM, c), _, _ in lst:
        for y in range(ym, yM + 1):
            out[y][x] = bg
    for i, ((x, ym, yM, c), _, _) in enumerate(lst):
        nl = NL[i]
        y_min = cy - nl // 2
        y_max = y_min + nl - 1
        y_min = max(0, y_min)
        y_max = min(h - 1, y_max)
        for y in range(y_min, y_max + 1):
            out[y][x] = c
    return out