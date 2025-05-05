from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    greys = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 4]
    rows = {}
    cols = {}
    for r, c in greys:
        rows.setdefault(r, []).append(c)
        cols.setdefault(c, []).append(r)
    for r, clist in rows.items():
        if len(clist) >= 2:
            c0, c1 = min(clist), max(clist)
            seg = [grid[r][c] for c in range(c0+1, c1)]
            S = set(seg)
            if len(S) == 2:
                s0, s1 = sorted(S)
                if S & {0, 6}:
                    m0, m1 = 7, 8
                else:
                    m0, m1 = 0, 6
                mp = {s0: m1, s1: m0}
                for c in range(c0+1, c1):
                    v = grid[r][c]
                    if v in mp:
                        out[r][c] = mp[v]
    for c, rlist in cols.items():
        if len(rlist) >= 2:
            r0, r1 = min(rlist), max(rlist)
            seg = [grid[r][c] for r in range(r0+1, r1)]
            S = set(seg)
            if len(S) == 2:
                s0, s1 = sorted(S)
                if S & {0, 6}:
                    m0, m1 = 7, 8
                else:
                    m0, m1 = 0, 6
                mp = {s0: m1, s1: m0}
                for r in range(r0+1, r1):
                    v = grid[r][c]
                    if v in mp:
                        out[r][c] = mp[v]
    return out