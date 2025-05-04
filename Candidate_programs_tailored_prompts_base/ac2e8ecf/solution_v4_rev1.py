from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    clusters = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0 and not visited[r][c]:
                col = grid[r][c]
                comp = [(r,c)]
                visited[r][c] = True
                q = [(r,c)]
                for rr, cc in q:
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and grid[nr][nc] == col:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                            comp.append((nr,nc))
                rs = [p[0] for p in comp]
                cs = [p[1] for p in comp]
                min_r, max_r = min(rs), max(rs)
                min_c, max_c = min(cs), max(cs)
                h = max_r - min_r + 1
                w = max_c - min_c + 1
                clusters.append({
                    'cells': comp, 'col': col,
                    'min_r': min_r, 'min_c': min_c,
                    'h': h, 'w': w
                })
    ring = []
    nonring = []
    for cl in clusters:
        mr, mc, h, w = cl['min_r'], cl['min_c'], cl['h'], cl['w']
        if h >= 3 and w >= 3 and all(
            grid[r][c] == 0
            for r in range(mr+1, mr+h-1)
            for c in range(mc+1, mc+w-1)
        ):
            ring.append(cl)
        else:
            nonring.append(cl)
    ring.sort(key=lambda x: x['min_r'])
    nonring.sort(key=lambda x: x['min_r'])
    occ = [[False]*W for _ in range(H)]
    for cl in ring:
        or0 = 0
        oc0 = cl['min_c']
        while True:
            conflict = False
            for r, c in cl['cells']:
                dr = r - cl['min_r']
                dc = c - cl['min_c']
                rr, cc = or0 + dr, oc0 + dc
                if occ[rr][cc]:
                    conflict = True
                    break
            if conflict:
                or0 += 1
            else:
                for r, c in cl['cells']:
                    dr = r - cl['min_r']
                    dc = c - cl['min_c']
                    occ[or0+dr][oc0+dc] = True
                cl['or'], cl['oc'] = or0, oc0
                break
    occ2 = [[False]*W for _ in range(H)]
    for cl in nonring:
        or0 = H - cl['h']
        oc0 = cl['min_c']
        while True:
            conflict = False
            for r, c in cl['cells']:
                dr = r - cl['min_r']
                dc = c - cl['min_c']
                rr, cc = or0 + dr, oc0 + dc
                if occ2[rr][cc]:
                    conflict = True
                    break
            if conflict:
                or0 -= 1
            else:
                for r, c in cl['cells']:
                    dr = r - cl['min_r']
                    dc = c - cl['min_c']
                    occ2[or0+dr][oc0+dc] = True
                cl['or'], cl['oc'] = or0, oc0
                break
    out = [[0]*W for _ in range(H)]
    for cl in ring + nonring:
        for r, c in cl['cells']:
            dr = r - cl['min_r']
            dc = c - cl['min_c']
            out[cl['or']+dr][cl['oc']+dc] = cl['col']
    return out