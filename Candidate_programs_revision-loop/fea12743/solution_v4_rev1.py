from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    zr = [i for i in range(h) if all(x == 0 for x in grid[i])]
    zc = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    rs = [zr[k]+1 for k in range(len(zr)-1)]
    re = [zr[k+1] for k in range(len(zr)-1)]
    cs = [zc[k]+1 for k in range(len(zc)-1)]
    ce = [zc[k+1] for k in range(len(zc)-1)]
    blocks = []
    for bi in range(len(rs)):
        for bj in range(len(cs)):
            cnt = 0
            for i in range(rs[bi], re[bi]):
                for j in range(cs[bj], ce[bj]):
                    if grid[i][j] == 2:
                        cnt += 1
            blocks.append((cnt, bi, bj))
    maxcnt = max(b[0] for b in blocks)
    out = [row[:] for row in grid]
    for cnt, bi, bj in blocks:
        if cnt == maxcnt:
            c = 3
        elif (bi + bj) % 2 == 0:
            c = 2
        else:
            c = 8
        for i in range(rs[bi], re[bi]):
            for j in range(cs[bj], ce[bj]):
                if grid[i][j] == 2:
                    out[i][j] = c
    return out