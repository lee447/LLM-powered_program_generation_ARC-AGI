import numpy as np
def solve(grid):
    h, w = len(grid), len(grid[0])
    ones = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1]
    def pivot(ps):
        nbr = {p:0 for p in ps}
        s = set(ps)
        for r,c in ps:
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                if (r+dr,c+dc) in s:
                    nbr[(r,c)] += 1
        m = max(nbr.values())
        cands = [p for p,n in nbr.items() if n==m]
        best = min(cands, key=lambda p: sum(abs(p[0]-q[0])+abs(p[1]-q[1]) for q in ps))
        return best
    pr, pc = pivot(ones)
    template = [(r-pr, c-pc) for r, c in ones]
    cnt = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v not in (0,1):
                cnt[v] = cnt.get(v, 0) + 1
    seeds = [(r, c, grid[r][c]) for r in range(h) for c in range(w)
             if grid[r][c] not in (0,1) and cnt[grid[r][c]] == 1]
    out = [row[:] for row in grid]
    for sr, sc, v in seeds:
        dr_s, dc_s = sr - pr, sc - pc
        if abs(dc_s) > abs(dr_s):
            tgt = "right" if dc_s > 0 else "left"
        else:
            tgt = "down" if dr_s > 0 else "up"
        for dr0, dc0 in template:
            if tgt == "down":
                r0, c0 = dr0, dc0
            elif tgt == "up":
                r0, c0 = -dr0, -dc0
            elif tgt == "right":
                r0, c0 = -dc0, dr0
            else:
                r0, c0 = dc0, -dr0
            rr, cc = sr + r0, sc + c0
            if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0:
                out[rr][cc] = v
    return out