import math
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    pts = [(i, j) for i in range(R) for j in range(C) if grid[i][j] != 0]
    if not pts:
        return [[0]*C for _ in range(R)]
    color = grid[pts[0][0]][pts[0][1]]
    rows = [i for i,_ in pts]; cols = [j for _,j in pts]
    r0, r1 = min(rows), max(rows)
    c0, c1 = min(cols), max(cols)
    h = r1 - r0 + 1; w = c1 - c0 + 1
    C0 = color; D = 9 - C0
    T = h + w
    out = [[0]*C for _ in range(R)]
    kr = range(-(R//T+2), R//T+3)
    kc = range(-(C//T+2), C//T+3)
    for k in kr:
        for l in kc:
            if k==0 and l==0: continue
            i0 = r0 + k*T; j0 = c0 + l*T
            for di in range(h):
                for dj in range(w):
                    i, j = i0+di, j0+dj
                    if 0 <= i < R and 0 <= j < C:
                        out[i][j] = C0
    for k in kr:
        for l in kc:
            for bi in (r0 - w, r0 + h):
                for bj in (c0 - h, c0 + w):
                    i0 = bi + k*T; j0 = bj + l*T
                    for di in range(w):
                        for dj in range(h):
                            i, j = i0+di, j0+dj
                            if 0 <= i < R and 0 <= j < C:
                                out[i][j] = D
    return out