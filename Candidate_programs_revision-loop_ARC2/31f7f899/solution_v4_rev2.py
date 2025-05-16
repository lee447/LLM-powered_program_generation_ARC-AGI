from typing import List
import math

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = 8
    vert = {}
    for x in range(w):
        ys = [y for y in range(h) if grid[y][x] != bg]
        if len(ys) > 1:
            vert[x] = ys
    bigx, bigys = max(vert.items(), key=lambda kv: len(kv[1]))
    y0, y1 = min(bigys), max(bigys)
    small = []
    for x, ys in vert.items():
        if x == bigx: continue
        ym, yM = min(ys), max(ys)
        small.append((x, ym, yM, grid[ym][x]))
    small.sort(key=lambda t: t[0])
    L = [yM - ym + 1 for _, ym, yM, _ in small]
    NL = list(reversed(L))
    big_len = y1 - y0 + 1
    out = [row[:] for row in grid]
    for x, ym, yM, _ in small:
        for y in range(ym, yM+1):
            out[y][x] = bg
    for (x, _, _, c), nl in zip(small, NL):
        slack = big_len - nl
        if x < bigx:
            shift = math.ceil(slack/2)
        else:
            shift = slack//2
        y_min = y0 + shift
        y_max = y_min + nl - 1
        for y in range(y_min, y_max+1):
            out[y][x] = c
    return out