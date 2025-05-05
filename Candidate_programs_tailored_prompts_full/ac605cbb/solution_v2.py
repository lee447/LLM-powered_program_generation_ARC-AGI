def solve(grid):
    H, W = len(grid), len(grid[0])
    anchors = [(r, c, grid[r][c]) for r in range(H) for c in range(W) if grid[r][c] != 0]
    out = [[0]*W for _ in range(H)]
    occ = set()
    for r, c, v in anchors:
        out[r][c] = v
        occ.add((r, c))
    for r, c, v in anchors:
        found = None
        for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            hx_max = W-1-c if dx>0 else c
            vy_max = H-1-r if dy>0 else r
            for total in range(2, hx_max+vy_max+1):
                for hx in range(1, min(hx_max, total-1)+1):
                    vy = total - hx
                    if not (1 <= vy <= vy_max): continue
                    ok = True
                    for i in range(1, hx+1):
                        p = (r, c+dx*i)
                        if p in occ: ok=False; break
                    if not ok: continue
                    corner = (r, c+dx*hx)
                    for j in range(1, vy+1):
                        p = (r+dy*j, corner[1])
                        if p in occ: ok=False; break
                    if not ok: continue
                    found = (hx, vy, dx, dy)
                    break
                if found: break
            if found: break
        if not found:
            # try straight horizontal
            for dx in (1, -1):
                hx_max = W-1-c if dx>0 else c
                for hx in range(1, hx_max+1):
                    ok = True
                    for i in range(1, hx+1):
                        p = (r, c+dx*i)
                        if p in occ: ok=False; break
                    if ok:
                        found = (hx, 0, dx, 0)
                        break
                if found: break
        if not found:
            # try straight vertical
            for dy in (1, -1):
                vy_max = H-1-r if dy>0 else r
                for vy in range(1, vy_max+1):
                    ok = True
                    for j in range(1, vy+1):
                        p = (r+dy*j, c)
                        if p in occ: ok=False; break
                    if ok:
                        found = (0, vy, 0, dy)
                        break
                if found: break
        if not found:
            continue
        hx, vy, dx, dy = found
        if hx > 0 and vy > 0:
            corner = (r, c+dx*hx)
            out[corner[0]][corner[1]] = 4
            occ.add(corner)
        for i in range(1, hx+1):
            p = (r, c+dx*i)
            out[p[0]][p[1]] = 5
            occ.add(p)
        for j in range(1, vy+1):
            p = (r+dy*j, c+dx*hx)
            out[p[0]][p[1]] = 5
            occ.add(p)
        end = (r+dy*vy, c+dx*hx)
        out[end[0]][end[1]] = v
        occ.add(end)
    return out