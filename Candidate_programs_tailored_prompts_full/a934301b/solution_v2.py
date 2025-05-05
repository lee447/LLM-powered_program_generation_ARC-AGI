def solve(grid):
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
                size = max(maxy-miny+1, maxx-minx+1)
                anchor = next((p for p in pts if p[2] == 8), None)
                clusters.append({
                    'pts': pts,
                    'miny': miny, 'minx': minx,
                    'size': size,
                    'anchor': (anchor[0], anchor[1]) if anchor else None
                })
    if not clusters:
        return grid
    # group rows by miny
    rows = sorted({c['miny'] for c in clusters})
    cols = sorted({c['minx'] for c in clusters})
    R, C = len(rows), len(cols)
    # assign indices
    for c in clusters:
        c['ri'] = min(range(R), key=lambda i: abs(rows[i]-c['miny']))
        c['ci'] = min(range(C), key=lambda j: abs(cols[j]-c['minx']))
    # decide stripe
    S = clusters[0]['size']
    if S % 2 == 1:
        # column stripe
        ci_keep = C - 1
        keep = [c for c in clusters if c['ci'] == ci_keep]
    else:
        # row stripe
        if R % 2 == 0:
            ri_keep = 0
        else:
            ri_keep = R // 2
        keep = [c for c in clusters if c['ri'] == ri_keep]
    out = [[0]*W for _ in range(H)]
    for c in keep:
        for y, x, v in c['pts']:
            out[y][x] = v
    return out