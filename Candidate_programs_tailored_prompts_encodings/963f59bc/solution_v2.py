from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    # find the single 1‐cluster by BFS
    found = False
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                sr, sc = i, j
                found = True
                break
        if found: break
    q = deque([(sr, sc)])
    cluster = {(sr, sc)}
    while q:
        r, c = q.popleft()
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            rr, cc = r+dr, c+dc
            if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 1 and (rr,cc) not in cluster:
                cluster.add((rr,cc))
                q.append((rr,cc))
    cluster = list(cluster)
    # find template center = cell with minimal sum of distances
    best_sum = None
    for (r, c) in cluster:
        s = sum(abs(r-r2)+abs(c-c2) for (r2, c2) in cluster)
        if best_sum is None or s < best_sum:
            best_sum = s
            cr, cc0 = r, c
    # compute relative coords
    rel = [(r-cr, c-cc0) for (r, c) in cluster]
    # collect single‐cell seeds (value !=0,1)
    seeds = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] not in (0,1)]
    out = [row[:] for row in grid]
    for r0, c0, v in seeds:
        for dr, dc in rel:
            if v in (3,6):
                dr2, dc2 = dc, -dr
            elif v in (2,8):
                dr2, dc2 = -dr, -dc
            else:
                dr2, dc2 = dr, dc
            rr, cc = r0+dr2, c0+dc2
            if 0 <= rr < h and 0 <= cc < w:
                out[rr][cc] = v
    return out