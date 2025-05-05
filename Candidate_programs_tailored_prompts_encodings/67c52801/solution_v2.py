from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    border = grid[h-1][0]
    base_top = h - 2
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for r in range(base_top):
        for c in range(w):
            if not visited[r][c] and grid[r][c] not in (0, border):
                val = grid[r][c]
                queue = [(r,c)]
                visited[r][c] = True
                coords = []
                mi, ma, mj, mb = r, r, c, c
                for rr,cc in queue:
                    coords.append((rr,cc))
                    mi = min(mi, rr); ma = max(ma, rr)
                    mj = min(mj, cc); mb = max(mb, cc)
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < base_top and 0 <= nc < w and not visited[nr][nc]:
                            if grid[nr][nc] == val:
                                visited[nr][nc] = True
                                queue.append((nr,nc))
                clusters.append({'min_c': mj, 'h0': ma-mi+1, 'w0': mb-mj+1, 'val': val})
    pillar = [c for c in range(w) if grid[base_top][c] == border]
    pillar.sort()
    slots = []
    prev = -1
    for p in pillar:
        if p - prev - 1 > 0:
            slots.append((prev+1, p-prev-1))
        prev = p
    if w-1 - prev > 0:
        slots.append((prev+1, w-1-prev))
    assigned = {}
    used = set()
    for si, (sc, sw) in enumerate(slots):
        cand = []
        for i, cl in enumerate(clusters):
            if i in used:
                continue
            h0, w0 = cl['h0'], cl['w0']
            wo = w0 if h0==2 else h0
            if wo == sw:
                cand.append((cl['min_c'], i))
        _, ci = min(cand)
        assigned[si] = clusters[ci]
        used.add(ci)
    out = [[0]*w for _ in range(h)]
    for r in range(base_top, h):
        out[r] = grid[r].copy()
    for si, (sc, sw) in enumerate(slots):
        cl = assigned[si]
        h0, w0, val = cl['h0'], cl['w0'], cl['val']
        H = 2
        W = w0 if h0==2 else h0
        for dr in range(H):
            ro = base_top-1 + dr
            for dc in range(W):
                out[ro][sc+dc] = val
    return out