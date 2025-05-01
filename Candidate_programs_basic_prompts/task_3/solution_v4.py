def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import deque
    # find clusters of nonzero pixels
    seen = [[False]*w for _ in range(h)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    res = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                # BFS cluster
                q = deque([(i,j)])
                seen[i][j] = True
                coords = []
                while q:
                    r,c = q.popleft()
                    coords.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]!=0 and not seen[nr][nc]:
                            seen[nr][nc] = True
                            q.append((nr,nc))
                # interior mask: pixel with all 4 nbrs nonzero
                interior = set()
                for r,c in coords:
                    ok = True
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if not (0<=nr<h and 0<=nc<w and grid[nr][nc]!=0):
                            ok = False
                            break
                    if ok:
                        interior.add((r,c))
                if not interior:
                    continue
                # components of interior pixels
                comp_id = {}
                comps = []
                for p in interior:
                    if p not in comp_id:
                        cid = len(comps)
                        comps.append([])
                        dq = deque([p])
                        comp_id[p] = cid
                        while dq:
                            x,y = dq.popleft()
                            comps[cid].append((x,y))
                            for dr,dc in dirs:
                                nx, ny = x+dr, y+dc
                                if (nx,ny) in interior and (nx,ny) not in comp_id:
                                    comp_id[(nx,ny)] = cid
                                    dq.append((nx,ny))
                # rep coords and seed detection
                rep = {}
                seed_list = []
                for cid, pts in enumerate(comps):
                    rep_pt = pts[0]
                    rep[cid] = rep_pt
                    for (r,c) in pts:
                        if grid[r][c] > 1:
                            seed_list.append((cid, grid[r][c]))
                            break
                # compute comp grid indices
                rows = sorted({r for (r,c) in rep.values()})
                cols = sorted({c for (r,c) in rep.values()})
                comp_pos = {}
                for cid, (r,c) in rep.items():
                    ri = rows.index(r)
                    ci = cols.index(c)
                    comp_pos[cid] = (ri, ci)
                # propagate seeds
                comp_color = {}
                seed_list.sort(key=lambda x: comp_pos[x[0]])
                for cid, val in seed_list:
                    comp_color[cid] = val
                for cid, val in seed_list:
                    ri, ci = comp_pos[cid]
                    for cid2 in range(len(comps)):
                        if cid2 not in comp_color:
                            r2, c2 = comp_pos[cid2]
                            if r2 == ri or c2 == ci:
                                comp_color[cid2] = val
                # fill
                for cid, pts in enumerate(comps):
                    v = comp_color.get(cid)
                    if v is None:
                        continue
                    for r,c in pts:
                        res[r][c] = v
    return res