def solve(grid):
    from collections import Counter, deque
    H, W = len(grid), len(grid[0])
    cnt = Counter(val for row in grid for val in row)
    bg, _ = cnt.most_common()[-1]
    # find components of non-bg cells
    used = [[False]*W for _ in range(H)]
    comps = []
    for r in range(H):
        for c in range(W):
            if grid[r][c]!=bg and not used[r][c]:
                val = grid[r][c]
                q = deque([(r,c)])
                used[r][c] = True
                cells = []
                while q:
                    x,y = q.popleft()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<H and 0<=ny<W and not used[nx][ny] and grid[nx][ny]!=bg:
                            used[nx][ny]=True
                            q.append((nx,ny))
                # find center: color occurring exactly once
                freq = Counter(grid[x][y] for x,y in cells)
                center_color = min((col for col,cnt in freq.items() if cnt==1), default=None)
                if center_color is None:
                    # fallback: choose the min-color
                    center_color = min(freq)
                center = next((x,y) for x,y in cells if grid[x][y]==center_color)
                offs = [(x-center[0],y-center[1]) for x,y in cells]
                comp = {"center":center, "color":center_color, "cells":cells, "offs":offs}
                comps.append(comp)
    # group by center_color
    groups = {}
    for comp in comps:
        groups.setdefault(comp["color"], []).append(comp)
    new = [[bg]*W for _ in range(H)]
    for color, group in groups.items():
        # find isolated comp (offs only zero)
        iso = next((g for g in group if len(g["offs"])==1), None)
        if iso:
            tr, tc = iso["center"]
        else:
            tr = tc = None
        for g in group:
            cr, cc = g["center"]
            # detect orientation
            drs = [dr for dr,dc in g["offs"] if dc==0 and dr!=0]
            dcs = [dc for dr,dc in g["offs"] if dr==0 and dc!=0]
            if drs and not dcs and tr is not None:
                dr_shift = tr - cr
                dc_shift = 0
            elif dcs and not drs and tc is not None:
                dr_shift = 0
                dc_shift = tc - cc
            elif dcs and drs and tc is not None:
                dr_shift = 0
                dc_shift = tc - cc
            elif drs and dcs and tr is not None:
                dr_shift = tr - cr
                dc_shift = 0
            else:
                dr_shift = dc_shift = 0
            for dr,dc in g["offs"]:
                nr, nc = cr+dr+dr_shift, cc+dc+dc_shift
                if 0<=nr<H and 0<=nc<W:
                    new[nr][nc] = grid[cr+dr][cc+dc]
    return new