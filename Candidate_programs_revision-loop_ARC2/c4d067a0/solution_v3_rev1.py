from collections import deque, Counter
def solve(grid):
    n, m = len(grid), len(grid[0])
    bg = Counter(c for row in grid for c in row).most_common(1)[0][0]
    out = [row[:] for row in grid]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def find_clusters(color):
        vis = [[False]*m for _ in range(n)]
        clusters = []
        for i in range(n):
            for j in range(m):
                if grid[i][j]==color and not vis[i][j]:
                    q = deque([(i,j)])
                    vis[i][j]=True
                    pts = []
                    r0,r1,c0,c1 = i,i,j,j
                    while q:
                        x,y = q.popleft()
                        pts.append((x,y))
                        for dx,dy in dirs:
                            nx,ny = x+dx, y+dy
                            if 0<=nx<n and 0<=ny<m and not vis[nx][ny] and grid[nx][ny]==color:
                                vis[nx][ny]=True
                                q.append((nx,ny))
                                r0,r1 = min(r0,nx), max(r1,nx)
                                c0,c1 = min(c0,ny), max(c1,ny)
                    clusters.append((pts, r0, r1, c0, c1))
        return clusters
    colors = {grid[i][j] for i in range(n) for j in range(m)}-{bg}
    for c in colors:
        cls = find_clusters(c)
        if not cls: continue
        maxsz = max(len(p) for p,_,_,_,_ in cls)
        templ = next((p,r0,r1,c0,c1) for p,r0,r1,c0,c1 in cls if len(p)==maxsz)
        pts, r0, r1, c0, c1 = templ
        bh, bw = r1-r0+1, c1-c0+1
        mask = [[False]*bw for _ in range(bh)]
        for x,y in pts:
            mask[x-r0][y-c0] = True
        origins = [(r0_,c0_) for p_,r0_,r1_,c0_,c1_ in cls if len(p_)==maxsz]
        ys = sorted({y for y,_ in origins})
        xs = sorted({x for _,x in origins})
        if len(ys)>1: step_y = ys[1]-ys[0]
        else: step_y = bh
        if len(xs)>1: step_x = xs[1]-xs[0]
        else: step_x = bw
        oy, ox = ys[0], xs[0]
        for i in range(oy, n-bh+1, step_y):
            for j in range(ox, m-bw+1, step_x):
                found = any(grid[i+di][j+dj]==c for di in range(bh) for dj in range(bw) if mask[di][dj])
                if not found:
                    ok = True
                    for di in range(bh):
                        for dj in range(bw):
                            if mask[di][dj] and grid[i+di][j+dj]!=bg:
                                ok = False; break
                        if not ok: break
                    if ok:
                        for di in range(bh):
                            for dj in range(bw):
                                if mask[di][dj]:
                                    out[i+di][j+dj] = c
    return out