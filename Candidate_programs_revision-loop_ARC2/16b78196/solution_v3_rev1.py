import numpy as np
from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def find_comps(cond):
        seen = [[False]*w for _ in range(h)]
        comps = []
        for i in range(h):
            for j in range(w):
                if not seen[i][j] and cond(grid[i][j]):
                    c = grid[i][j]
                    q = deque([(i,j)])
                    seen[i][j] = True
                    pts = []
                    while q:
                        x,y = q.popleft()
                        pts.append((x,y))
                        for dx,dy in dirs:
                            nx,ny = x+dx, y+dy
                            if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==c:
                                seen[nx][ny] = True
                                q.append((nx,ny))
                    xs = [p[1] for p in pts]
                    ys = [p[0] for p in pts]
                    comps.append({
                        'color': c,
                        'pts': pts,
                        'minx': min(xs),
                        'maxx': max(xs),
                        'miny': min(ys),
                        'maxy': max(ys)
                    })
        return comps

    bg_comps = find_comps(lambda c: c==8)
    bg = max(bg_comps, key=lambda c: (c['maxy']-c['miny']+1)*(c['maxx']-c['minx']+1))
    miny8, maxy8 = bg['miny'], bg['maxy']
    comps = find_comps(lambda c: c!=0 and c!=8)
    above = [c for c in comps if c['maxy']<miny8]
    below = [c for c in comps if c['miny']>maxy8]
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if out[i][j]!=8:
                out[i][j] = 0

    def draw(c, y0, x0):
        for y,x in c['pts']:
            out[y0 + (y-c['miny'])][x0 + (x-c['minx'])] = c['color']

    below_sorted = sorted(below, key=lambda c: c['minx'])
    x = 0
    for c in below_sorted:
        height = c['maxy']-c['miny']+1
        y0 = miny8 - height
        draw(c, y0, x)
        x += (c['maxx']-c['minx']+1) + 1

    above_sorted = sorted(above, key=lambda c: c['minx'])
    x = 0
    for c in above_sorted:
        y0 = maxy8 + 1
        draw(c, y0, x)
        x += (c['maxx']-c['minx']+1) + 1

    return out