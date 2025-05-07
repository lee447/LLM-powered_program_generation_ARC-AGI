from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    zr = [i for i in range(h) if all(x == 0 for x in grid[i])]
    zc = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    rs = [zr[k] + 1 for k in range(len(zr) - 1)]
    re = [zr[k + 1] for k in range(len(zr) - 1)]
    cs = [zc[k] + 1 for k in range(len(zc) - 1)]
    ce = [zc[k + 1] for k in range(len(zc) - 1)]
    R, C = len(rs), len(cs)
    cnt = [[0] * C for _ in range(R)]
    for bi in range(R):
        for bj in range(C):
            c0 = 0
            for i in range(rs[bi], re[bi]):
                for j in range(cs[bj], ce[bj]):
                    if grid[i][j] == 2:
                        c0 += 1
            cnt[bi][bj] = c0
    flat = [(cnt[bi][bj], bi, bj) for bi in range(R) for bj in range(C)]
    maxcnt = max(v for v, _, _ in flat)
    sel = [t for t in flat if t[0] == maxcnt]
    if len(sel) == 1:
        _, si, sj = sel[0]
    else:
        _, si, sj = max(flat, key=lambda t: (t[1], t[2]))
    sum_even = sum(cnt[bi][bj] for bi in range(R) for bj in range(C) if (bi + bj) % 2 == 0)
    sum_odd = sum(cnt[bi][bj] for bi in range(R) for bj in range(C) if (bi + bj) % 2 == 1)
    if sum_even > sum_odd:
        ceven, codd = 2, 8
    else:
        ceven, codd = 8, 2
    out = [row[:] for row in grid]
    for bi in range(R):
        for bj in range(C):
            if bi == si and bj == sj:
                c = 3
            else:
                c = ceven if (bi + bj) % 2 == 0 else codd
            for i in range(rs[bi], re[bi]):
                for j in range(cs[bj], ce[bj]):
                    if grid[i][j] == 2:
                        out[i][j] = c
    return out