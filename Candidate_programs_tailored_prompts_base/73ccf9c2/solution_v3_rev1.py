import math
from itertools import combinations
def solve(grid):
    R, C = len(grid), len(grid[0])
    val = next((grid[i][j] for i in range(R) for j in range(C) if grid[i][j] != 0), 0)
    visited = [[False]*C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == val and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                        nr,nc = r+dr,c+dc
                        if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and grid[nr][nc]==val:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                comps.append(comp)
    if not comps:
        return []
    comps.sort(key=len, reverse=True)
    sets = []
    for comp in comps:
        rs = [r for r,c in comp]; cs = [c for r,c in comp]
        mn_r, mx_r = min(rs), max(rs)
        mn_c, mx_c = min(cs), max(cs)
        center_r = (mn_r + mx_r)/2.0
        center_c = (mn_c + mx_c)/2.0
        cr = int(math.floor(center_r+0.5))
        cc = int(math.floor(center_c+0.5))
        sets.append({(r-cr, c-cc) for r,c in comp})
    best = set()
    n = len(sets)
    found = False
    for k in (3,2):
        if n >= k:
            S = sets[0].copy()
            for s in sets[1:k]:
                S &= s
            if S:
                best = S
                found = True
                break
    if not found:
        best = sets[0]
    drs = [dr for dr,dc in best]; dcs = [dc for dr,dc in best]
    min_dr, max_dr = min(drs), max(drs)
    min_dc, max_dc = min(dcs), max(dcs)
    H = max_dr - min_dr + 1
    W = max_dc - min_dc + 1
    out = [[0]*W for _ in range(H)]
    for dr,dc in best:
        out[dr-min_dr][dc-min_dc] = val
    return out