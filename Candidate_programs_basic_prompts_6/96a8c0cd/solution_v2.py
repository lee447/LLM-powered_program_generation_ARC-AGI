from typing import List, Tuple

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    # find seed (unique 2)
    seeds = [(y, x) for y in range(h) for x in range(w) if g[y][x] == 2]
    seeds = sorted(seeds)
    if seeds:
        cy, cx = seeds[0]
    else:
        cy = cx = 0
    # find clusters of non-zero/non-2
    seen = [[False]*w for _ in range(h)]
    centers: List[Tuple[int,int]] = []
    for y in range(h):
        for x in range(w):
            if g[y][x] not in (0,2) and not seen[y][x]:
                col = g[y][x]
                stack = [(y,x)]
                seen[y][x] = True
                pts = []
                while stack:
                    yy, xx = stack.pop()
                    pts.append((yy, xx))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0 <= ny < h and 0 <= nx < w and not seen[ny][nx] and g[ny][nx]==col:
                            seen[ny][nx] = True
                            stack.append((ny,nx))
                ay = sum(p[0] for p in pts)/len(pts)
                ax = sum(p[1] for p in pts)/len(pts)
                cyc = int(round(ay))
                cxc = int(round(ax))
                centers.append((cyc, cxc))
    centers.sort()
    for ty, tx in centers:
        # horizontal
        while cx != tx:
            dx = 1 if tx > cx else -1
            cx += dx
            if 0 <= cy < h and 0 <= cx < w and g[cy][cx] == 0:
                g[cy][cx] = 2
        # vertical
        while cy != ty:
            dy = 1 if ty > cy else -1
            cy += dy
            if 0 <= cy < h and 0 <= cx < w and g[cy][cx] == 0:
                g[cy][cx] = 2
    return g