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
                        'maxy': max(ys),
                        'area': len(pts)
                    })
        return comps

    nonzero = find_comps(lambda c: c!=0)
    bg = max(nonzero, key=lambda c: c['area'])
    bg_color = bg['color']
    miny, maxy = bg['miny'], bg['maxy']
    shapes = find_comps(lambda c: c!=0 and c!=bg_color)
    above = [c for c in shapes if c['maxy'] < miny]
    below = [c for c in shapes if c['miny'] > maxy]

    out = [[0]*w for _ in range(h)]
    for y,x in bg['pts']:
        out[y][x] = bg_color

    def draw(c, y0, x0):
        for y,x in c['pts']:
            out[y0 + (y - c['miny'])][x0 + (x - c['minx'])] = c['color']

    above_sorted = sorted(above, key=lambda c: c['minx'])
    x0 = 0
    for c in above_sorted:
        h0 = c['maxy'] - c['miny'] + 1
        y0 = miny - h0
        draw(c, y0, x0)
        x0 += (c['maxx'] - c['minx'] + 1) + 1

    below_sorted = sorted(below, key=lambda c: c['minx'])
    x0 = 0
    for c in below_sorted:
        y0 = maxy + 1
        draw(c, y0, x0)
        x0 += (c['maxx'] - c['minx'] + 1) + 1

    return out