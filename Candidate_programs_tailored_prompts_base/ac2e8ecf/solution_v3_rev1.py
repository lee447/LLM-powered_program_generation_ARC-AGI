from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    clusters = []
    for y in range(h):
        for x in range(w):
            c = grid[y][x]
            if c != 0 and not vis[y][x]:
                pts = []
                stack = [(y,x)]
                vis[y][x] = True
                while stack:
                    yy, xx = stack.pop()
                    pts.append((yy,xx))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx]==c:
                            vis[ny][nx] = True
                            stack.append((ny,nx))
                ys = [p[0] for p in pts]
                xs = [p[1] for p in pts]
                y0, y1 = min(ys), max(ys)
                x0, x1 = min(xs), max(xs)
                deg4 = False
                s = set(pts)
                for yy,xx in pts:
                    d = 0
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        if (yy+dy,xx+dx) in s:
                            d += 1
                    if d==4:
                        deg4 = True
                        break
                clusters.append({
                    'pts': pts, 'color': c,
                    'y0': y0, 'x0': x0, 'y1': y1, 'x1': x1,
                    'h': y1-y0+1, 'w': x1-x0+1,
                    'plus': deg4
                })
    frame = [c for c in clusters if not c['plus']]
    plus = [c for c in clusters if c['plus']]
    frame.sort(key=lambda c: c['x0'], reverse=True)
    res = [[0]*w for _ in range(h)]
    top = 0
    while frame:
        row = []
        occ = []
        for c in frame:
            ok = True
            for a,b in occ:
                if not (c['x1'] < a or c['x0'] > b):
                    ok = False
                    break
            if ok:
                row.append(c)
                occ.append((c['x0'], c['x1']))
        for c in row:
            for yy,xx in c['pts']:
                ny = yy - c['y0'] + top
                nx = xx
                res[ny][nx] = c['color']
            frame.remove(c)
        if row:
            top += max(c['h'] for c in row)
    if plus:
        ph = max(c['h'] for c in plus)
        base = h - ph
        for c in plus:
            for yy,xx in c['pts']:
                ny = yy - c['y0'] + base
                nx = xx
                res[ny][nx] = c['color']
    return res