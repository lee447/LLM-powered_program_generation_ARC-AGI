def solve(grid):
    h, w = len(grid), len(grid[0])
    C = next(c for row in grid for c in row if c != 0)
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == C and not vis[i][j]:
                stk = [(i,j)]
                pts = []
                vis[i][j] = True
                while stk:
                    y,x = stk.pop()
                    pts.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx]==C:
                            vis[ny][nx] = True
                            stk.append((ny,nx))
                ys = [y for y,x in pts]
                comps.append((min(ys), pts))
    comps.sort(key=lambda x: x[0])
    if len(comps) == 2:
        top, bot = comps[0][1], comps[1][1]
    else:
        top, bot = comps[0][1], comps[-1][1]
    def norm(pts):
        ys = [y for y,x in pts]; xs = [x for y,x in pts]
        r0,r1,c0,c1 = min(ys), max(ys), min(xs), max(xs)
        return set((y-r0, x-c0) for y,x in pts), (r1-r0+1, c1-c0+1), ((r0+r1)/2, (c0+c1)/2)
    A, (h0,w0), ctr0 = norm(top)
    B, (h1,w1), ctr1 = norm(bot)
    o = {}
    for y,x in A:
        ry = y - (ctr0[0] - (h0-1)/2)
        rx = x - (ctr0[1] - (w0-1)/2)
        o[(round(ry), round(rx))] = o.get((round(ry), round(rx)), 0) + 1
    inter = {}
    for y,x in B:
        ry = y - (ctr1[0] - (h1-1)/2)
        rx = x - (ctr1[1] - (w1-1)/2)
        key = (round(ry), round(rx))
        if key in o:
            inter[key] = True
    ys = [y for y,x in inter]
    xs = [x for y,x in inter]
    r0, c0 = int(min(ys)), int(min(xs))
    r1, c1 = int(max(ys)), int(max(xs))
    H, W = r1-r0+1, c1-c0+1
    res = [[0]*W for _ in range(H)]
    for y,x in inter:
        iy, ix = int(y)-r0, int(x)-c0
        if 0 <= iy < H and 0 <= ix < W:
            res[iy][ix] = C
    return res