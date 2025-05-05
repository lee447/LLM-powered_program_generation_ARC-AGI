from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    # find the 1‐cluster
    vis = [[False]*w for _ in range(h)]
    pts = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                sr, sc = i, j
                break
        else:
            continue
        break
    q = deque([(sr, sc)])
    vis[sr][sc] = True
    while q:
        r, c = q.popleft()
        pts.append((r, c))
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < h and 0 <= nc < w and not vis[nr][nc] and grid[nr][nc] == 1:
                vis[nr][nc] = True
                q.append((nr, nc))
    # bounding box
    minr = min(r for r,c in pts)
    minc = min(c for r,c in pts)
    maxr = max(r for r,c in pts)
    maxc = max(c for r,c in pts)
    H = maxr - minr + 1
    W = maxc - minc + 1
    shape = [(r-minr, c-minc) for r,c in pts]
    # transforms
    def I(rc): return rc
    def Hm(rc): return (rc[0], W-1-rc[1])
    def Vm(rc): return (H-1-rc[0], rc[1])
    def R90(rc): return (rc[1], H-1-rc[0])
    def R180(rc): return (H-1-rc[0], W-1-rc[1])
    def R270(rc): return (W-1-rc[1], rc[0])
    transforms = [I, Hm, Vm, R90, R180, R270]
    out = [row[:] for row in grid]
    # find seeds
    seeds = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] not in (0,1)]
    for sr, sc, v in seeds:
        for f in transforms:
            for ar, ac in shape:
                fr, fc = f((ar, ac))
                off_r = sr - fr
                off_c = sc - fc
                ok = True
                for rr, cc in shape:
                    tr, tc = f((rr, cc))
                    nr, nc = off_r + tr, off_c + tc
                    if not (0 <= nr < h and 0 <= nc < w):
                        ok = False
                        break
                    val = grid[nr][nc]
                    if (nr, nc) == (sr, sc):
                        if val != v:
                            ok = False
                            break
                    else:
                        if val != 0:
                            ok = False
                            break
                if ok:
                    for rr, cc in shape:
                        tr, tc = f((rr, cc))
                        nr, nc = off_r + tr, off_c + tc
                        out[nr][nc] = v
                    sr = sc = v = None
                    break
            if sr is None:
                break
        if sr is not None:
            # fallback: no transform worked; do nothing
            pass
    return out