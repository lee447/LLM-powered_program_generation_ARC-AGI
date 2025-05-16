def solve(grid):
    from collections import deque
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    vis = [[False]*w for _ in range(h)]
    comps_by_color = {}
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c == bg or vis[y][x]:
                continue
            q = deque([(y, x)])
            vis[y][x] = True
            comp = [(y, x)]
            while q:
                cy, cx = q.popleft()
                for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                    ny, nx = cy+dy, cx+dx
                    if 0 <= ny < h and 0 <= nx < w and not vis[ny][nx] and grid[ny][nx]==c:
                        vis[ny][nx] = True
                        q.append((ny, nx))
                        comp.append((ny, nx))
            comps_by_color.setdefault(c, []).append(comp)
    ref = None
    for c, lc in comps_by_color.items():
        if len(lc)==4 and len({len(x) for x in lc})==1:
            ref = (c, lc)
            break
    if ref is None:
        return []
    refc, refcomps = ref
    pivots = {}
    for comp in refcomps:
        s = set(comp)
        for y,x in comp:
            cnt = 0
            if (y+1,x) in s and (y,x+1) in s:
                pivots['NW'] = (y, x)
            if (y+1,x) in s and (y,x-1) in s:
                pivots['NE'] = (y, x)
            if (y-1,x) in s and (y,x+1) in s:
                pivots['SW'] = (y, x)
            if (y-1,x) in s and (y,x-1) in s:
                pivots['SE'] = (y, x)
    pNW, pNE, pSW = pivots['NW'], pivots['NE'], pivots['SW']
    y0, x0 = pNW
    H = pivots['SW'][0] - y0 + 1
    W = pivots['NE'][1] - x0 + 1
    out = [[refc]*W for _ in range(H)]
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c==bg: continue
            yo = round((y - y0) * (H-1) / (pSW[0] - y0))
            xo = round((x - x0) * (W-1) / (pNE[1] - x0))
            out[yo][xo] = c
    return out