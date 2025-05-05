from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    colors = sorted({v for row in grid for v in row if v not in (0,2)})
    c1, c2 = colors
    rect = {c1: [H, W, -1, -1], c2: [H, W, -1, -1]}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v in rect:
                rr = rect[v]
                if r < rr[0]: rr[0] = r
                if c < rr[1]: rr[1] = c
                if r > rr[2]: rr[2] = r
                if c > rr[3]: rr[3] = c
    visited = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 2 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                comp = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==2:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                            comp.append((nx,ny))
                comps.append(comp)
    out = [row[:] for row in grid]
    for comp in comps:
        rs = [x for x,y in comp]
        cs = [y for x,y in comp]
        rmin, rmax = min(rs), max(rs)
        cmin, cmax = min(cs), max(cs)
        zone = None
        for x,y in comp:
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny = x+dx, y+dy
                if 0<=nx<H and 0<=ny<W and grid[nx][ny] in (c1,c2):
                    zone = grid[nx][ny]
                    break
            if zone is not None:
                break
        if zone is None:
            r1min,c1min,r1max,c1max = rect[c1]
            if r1min <= rmin <= r1max and c1min <= cmin <= c1max:
                zone = c1
            else:
                zone = c2
        zrmin, zrmin_c, zrmax, zrmax_c = rect[zone]
        for x,y in comp:
            out[x][y] = zone
        width = cmax - cmin + 1
        if zone == c1:
            dest_cmin = zrmax_c - width + 1
        else:
            dest_cmin = rect[zone][1]
        shift = dest_cmin - cmin
        for x,y in comp:
            out[x][y + shift] = 2
    return out