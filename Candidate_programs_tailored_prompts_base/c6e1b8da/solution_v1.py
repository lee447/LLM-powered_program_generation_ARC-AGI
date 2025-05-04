def solve(grid):
    from collections import deque
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                c = grid[i][j]
                q = deque([(i,j)])
                seen[i][j] = True
                pts = []
                mnr,mxr,mnc, mxc = i,i,j,j
                while q:
                    r,c0 = q.popleft()
                    pts.append((r,c0))
                    mnr,mxr = min(mnr,r), max(mxr,r)
                    mnc,mxc = min(mnc,c0), max(mxc,c0)
                    for dr,dc in dirs:
                        rr,cc = r+dr, c0+dc
                        if 0<=rr<h and 0<=cc<w and not seen[rr][cc] and grid[rr][cc]==grid[i][j]:
                            seen[rr][cc]=True
                            q.append((rr,cc))
                shapes.append({'color':grid[i][j],'pts':pts,'mnr':mnr,'mxr':mxr,'mnc':mnc,'mxc':mxc})
    anchor = next(s for s in shapes if s['color']==3)
    others = [s for s in shapes if s is not anchor]
    others.sort(key=lambda s: s['mnr'])
    out = [[0]*w for _ in range(h)]
    placed = set()
    for (r,c0) in anchor['pts']:
        out[r][c0] = 3
        placed.add((r,c0))
    prev = None
    for idx,s in enumerate(others):
        if idx==0:
            for (r,c0) in s['pts']:
                out[r][c0] = s['color']
                placed.add((r,c0))
            prev = s
            continue
        def fits(dx,dy):
            for (r,c0) in s['pts']:
                nr, nc = r+dy, c0+dx
                if not (0<=nr<h and 0<=nc<w): return False
                if (nr,nc) in placed: return False
            return True
        best = None
        # try horizontal right
        dx = prev['mxc']+1 - s['mnc']; dy = 0
        if fits(dx,dy): best=(dx,dy)
        else:
            # try horizontal left
            dx = prev['mnc']-1 - s['mxc']; dy=0
            if fits(dx,dy): best=(dx,dy)
            else:
                # vertical down
                dx=0; dy=prev['mxr']+1 - s['mnr']
                if fits(dx,dy): best=(dx,dy)
                else:
                    # vertical up
                    dy=prev['mnr']-1 - s['mxr']; dx=0
                    if fits(dx,dy): best=(dx,dy)
        if best is None: best=(0,0)
        dx,dy = best
        for (r,c0) in s['pts']:
            nr, nc = r+dy, c0+dx
            out[nr][nc] = s['color']
            placed.add((nr,nc))
        prev = {'mnc':s['mnc']+dx,'mxc':s['mxc']+dx,'mnr':s['mnr']+dy,'mxr':s['mxr']+dy}
    return out