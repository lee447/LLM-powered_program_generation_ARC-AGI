def solve(grid):
    H = len(grid)
    W = len(grid[0])
    vis = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j]==3 and not vis[i][j]:
                q = [(i,j)]
                vis[i][j]=True
                cells = []
                for y,x in q:
                    cells.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0<=ny<H and 0<=nx<W and grid[ny][nx]==3 and not vis[ny][nx]:
                            vis[ny][nx]=True
                            q.append((ny,nx))
                ys = [y for y,x in cells]
                xs = [x for y,x in cells]
                miny, maxy = min(ys), max(ys)
                minx, maxx = min(xs), max(xs)
                mask = [[0]*(maxx-minx+1) for _ in range(maxy-miny+1)]
                for y,x in cells:
                    mask[y-miny][x-minx] = 1
                comps.append((miny,minx,maxy,maxx,mask))
    comps.sort(key=lambda b:(b[0],b[1]))
    out = [row[:] for row in grid]
    cols = [1,8]
    n = len(comps)
    for i,(miny,minx,maxy,maxx,mask) in enumerate(comps):
        h = maxy-miny+1
        w = maxx-minx+1
        c = cols[i%2]
        placed=False
        for dy in range(-H,H+1):
            for dx in range(-W,W+1):
                if dy==0 and dx==0: continue
                ok=True
                for yy in range(h):
                    for xx in range(w):
                        if mask[yy][xx]:
                            ny = miny+dy+yy
                            nx = minx+dx+xx
                            if not(0<=ny<H and 0<=nx<W and out[ny][nx]==0):
                                ok=False
                                break
                    if not ok: break
                if ok:
                    for yy in range(h):
                        for xx in range(w):
                            if mask[yy][xx]:
                                out[miny+dy+yy][minx+dx+xx] = c
                    placed=True
                    break
            if placed: break
    return out