from typing import List
import math
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    clusters = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0 and not visited[r][c]:
                col = grid[r][c]
                q = deque([(r,c)])
                comp = []
                visited[r][c] = True
                while q:
                    rr, cc = q.popleft()
                    comp.append((rr,cc))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and grid[nr][nc] == col:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                if len(comp) >= 6:
                    rs = [p[0] for p in comp]
                    cs = [p[1] for p in comp]
                    min_r, max_r = min(rs), max(rs)
                    min_c, max_c = min(cs), max(cs)
                    h = max_r - min_r + 1
                    w = max_c - min_c + 1
                    cy = (min_r + max_r) / 2.0
                    cx = (min_c + max_c) / 2.0
                    clusters.append({
                        'cells': comp,
                        'color': col,
                        'min_r': min_r,
                        'min_c': min_c,
                        'h': h,
                        'w': w,
                        'cy': cy,
                        'cx': cx
                    })
    center_r = (H - 1) / 2.0
    center_c = (W - 1) / 2.0
    for cl in clusters:
        cl['angle'] = math.atan2(center_r - cl['cy'], cl['cx'] - center_c)
    clusters.sort(key=lambda x: x['angle'], reverse=True)
    main = clusters[:3]
    anchor = clusters[3] if len(clusters) > 3 else None
    out = [row[:] for row in grid]
    for cl in main + ([anchor] if anchor else []):
        for rr, cc in cl['cells']:
            out[rr][cc] = 0
    for i, cl in enumerate(main):
        if i == 0:
            or0, oc0 = 0, cl['min_c']
        elif i == 1:
            or0, oc0 = 0, cl['min_c']
        else:
            or0, oc0 = H - cl['h'], cl['min_c']
        for rr, cc in cl['cells']:
            dr, dc = rr - cl['min_r'], cc - cl['min_c']
            out[or0 + dr][oc0 + dc] = cl['color']
    if anchor:
        or0, oc0 = main[0]['h'], anchor['min_c']
        for rr, cc in anchor['cells']:
            dr, dc = rr - anchor['min_r'], cc - anchor['min_c']
            out[or0 + dr][oc0 + dc] = anchor['color']
    return out