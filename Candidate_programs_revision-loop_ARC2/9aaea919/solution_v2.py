def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if not seen[i][j] and grid[i][j] != bg:
                col = grid[i][j]
                pts = [(i,j)]
                seen[i][j] = True
                idx = 0
                while idx < len(pts):
                    y,x = pts[idx]; idx+=1
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and not seen[ny][nx] and grid[ny][nx]==col:
                            seen[ny][nx]=True
                            pts.append((ny,nx))
                ys = sorted(p[0] for p in pts)
                xs = sorted(p[1] for p in pts)
                cy = ys[len(ys)//2]
                cx = xs[len(xs)//2]
                offsets = [(y-cy,x-cx) for y,x in pts]
                clusters.append((cy,cx,col,offsets))
    ys = sorted({c[0] for c in clusters})
    xs = sorted({c[1] for c in clusters})
    new = [[bg]*w for _ in range(h)]
    for cy,cx,col,offs in clusters:
        r = ys.index(cy)
        c = xs.index(cx)
        ny = ys[c]
        nx = xs[r]
        for dy,dx in offs:
            new[ny+dy][nx+dx] = col
    return new