from typing import List, Tuple

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    vis = [[False]*W for _ in range(H)]
    clusters = []
    for y in range(H):
        for x in range(W):
            if grid[y][x] != 0 and not vis[y][x]:
                pts, q = [], [(y, x)]
                vis[y][x] = True
                while q:
                    cy, cx = q.pop()
                    pts.append((cy, cx, grid[cy][cx]))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < H and 0 <= nx < W and not vis[ny][nx] and grid[ny][nx] != 0:
                            vis[ny][nx] = True
                            q.append((ny, nx))
                ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
                miny, maxy, minx, maxx = min(ys), max(ys), min(xs), max(xs)
                clusters.append({
                    'pts': pts,
                    'miny': miny, 'minx': minx,
                    'h': maxy-miny+1, 'w': maxx-minx+1
                })
    if not clusters:
        return grid
    cols = sorted({c['minx'] for c in clusters})
    rows = sorted({c['miny'] for c in clusters})
    C, R = len(cols), len(rows)
    for c in clusters:
        c['ci'] = cols.index(c['minx'])
        c['ri'] = rows.index(c['miny'])
    if C < R:
        keep_cols = {i for i in range(C) if i >= C//2}
        out = [[0]*W for _ in range(H)]
        for c in clusters:
            if c['ci'] in keep_cols:
                for y,x,v in c['pts']:
                    out[y][x] = v
    else:
        keep_rows = {i for i in range(R) if i < R//2 + (R%2==0)}
        out = [[0]*W for _ in range(H)]
        for c in clusters:
            if c['ri'] in keep_rows:
                for y,x,v in c['pts']:
                    out[y][x] = v
    return out