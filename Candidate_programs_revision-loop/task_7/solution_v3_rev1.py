import math
def solve(grid):
    H, W = len(grid), len(grid[0])
    vis = [[False]*W for _ in range(H)]
    regions = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 4 and not vis[r][c]:
                comp = []
                stack = [(r,c)]
                vis[r][c] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not vis[nx][ny] and grid[nx][ny] != 4:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                regions.append(comp)
    master_idx = None
    master_color = None
    for i,comp in enumerate(regions):
        for x,y in comp:
            v = grid[x][y]
            if v not in (0,1,4):
                master_idx = i
                master_color = v
                break
        if master_idx is not None:
            break
    comp = regions[master_idx]
    rs = [x for x,y in comp]; cs = [y for x,y in comp]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    MH, MW = r1-r0+1, c1-c0+1
    mask = [[0]*MW for _ in range(MH)]
    for i in range(MH):
        for j in range(MW):
            if grid[r0+i][c0+j] == master_color:
                mask[i][j] = 1
    out = [row[:] for row in grid]
    for i,comp in enumerate(regions):
        if i == master_idx:
            continue
        vals = {grid[x][y] for x,y in comp}
        if not vals.issubset({0,1}):
            continue
        rs = [x for x,y in comp]; cs = [y for x,y in comp]
        rr0, rr1 = min(rs), max(rs)
        cc0, cc1 = min(cs), max(cs)
        h, w = rr1-rr0+1, cc1-cc0+1
        for x,y in comp:
            if grid[x][y] != 1:
                continue
            ic = x-rr0; jc = y-cc0
            if h>1:
                im = int(round(ic*(MH-1)/(h-1)))
            else:
                im = 0
            if w>1:
                jm = int(round(jc*(MW-1)/(w-1)))
            else:
                jm = 0
            if mask[im][jm]:
                out[x][y] = master_color
    return out