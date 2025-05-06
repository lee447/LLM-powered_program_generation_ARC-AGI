def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                pts = []
                vis[i][j] = True
                while stack:
                    y,x = stack.pop()
                    pts.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and not vis[ny][nx] and grid[ny][nx]==col:
                            vis[ny][nx] = True
                            stack.append((ny,nx))
                comps.append((col, pts))
    shapes = []
    for col, pts in comps:
        ys = [p[0] for p in pts]
        xs = [p[1] for p in pts]
        y0, y1 = min(ys), max(ys)
        x0, x1 = min(xs), max(xs)
        hh, ww = y1-y0+1, x1-x0+1
        if hh==ww:
            ok = True
            for y in range(y0, y1+1):
                for x in range(x0, x1+1):
                    if y==y0 or y==y1 or x==x0 or x==x1:
                        if grid[y][x]!=col: ok=False
                    else:
                        if grid[y][x]!=0: ok=False
                    if not ok: break
                if not ok: break
            if ok:
                block = [row[x0:x1+1] for row in grid[y0:y1+1]]
                shapes.append((y0, x0, block))
    if not shapes:
        return []
    n = len(shapes)
    if n==2:
        ymins = [s[0] for s in shapes]
        ymaxs = [s[0]+len(s[2])-1 for s in shapes]
        horizontal = max(ymins) <= min(ymaxs)
    else:
        horizontal = True
    if horizontal:
        shapes.sort(key=lambda s: s[1])
        out_h = len(shapes[0][2])
        out_w = sum(len(s[2][0]) for s in shapes)
        out = [[0]*out_w for _ in range(out_h)]
        cx = 0
        for _,_,blk in shapes:
            ww = len(blk[0])
            for y in range(out_h):
                for x in range(ww):
                    out[y][cx+x] = blk[y][x]
            cx += ww
    else:
        shapes.sort(key=lambda s: s[0])
        out_w = len(shapes[0][2][0])
        out_h = sum(len(s[2]) for s in shapes)
        out = [[0]*out_w for _ in range(out_h)]
        cy = 0
        for _,_,blk in shapes:
            hh = len(blk)
            for y in range(hh):
                for x in range(out_w):
                    out[cy+y][x] = blk[y][x]
            cy += hh
    return out