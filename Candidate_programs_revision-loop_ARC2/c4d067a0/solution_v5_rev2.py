import collections
def solve(grid):
    n, m = len(grid), len(grid[0])
    cnt = collections.Counter(c for row in grid for c in row)
    bg = cnt.most_common(1)[0][0]
    out = [row[:] for row in grid]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def find_clusters(color):
        vis = [[False]*m for _ in range(n)]
        cls = []
        for i in range(n):
            for j in range(m):
                if grid[i][j]==color and not vis[i][j]:
                    q = collections.deque([(i,j)])
                    vis[i][j]=True
                    pts = []
                    r0,r1,c0,c1 = i,i,j,j
                    while q:
                        x,y = q.popleft()
                        pts.append((x,y))
                        for dx,dy in dirs:
                            nx,ny = x+dx,y+dy
                            if 0<=nx<n and 0<=ny<m and not vis[nx][ny] and grid[nx][ny]==color:
                                vis[nx][ny]=True
                                q.append((nx,ny))
                                r0,r1 = min(r0,nx),max(r1,nx)
                                c0,c1 = min(c0,ny),max(c1,ny)
                    h,w = r1-r0+1, c1-c0+1
                    mask = [[False]*w for _ in range(h)]
                    for x,y in pts:
                        mask[x-r0][y-c0] = True
                    cls.append((r0,c0,h,w,mask,len(pts)))
        return cls
    for color in {grid[i][j] for i in range(n) for j in range(m)} - {bg}:
        cls = find_clusters(color)
        if not cls:
            continue
        mx = max(c[5] for c in cls)
        templ = [c for c in cls if c[5]==mx]
        r0s = sorted({c[0] for c in templ})
        c0s = sorted({c[1] for c in templ})
        h,w = templ[0][2], templ[0][3]
        mask = templ[0][4]
        if len(r0s)>1:
            step_x = min(r0s[i+1]-r0s[i] for i in range(len(r0s)-1))
            rows = list(range(r0s[0], n-h+1, step_x))
        else:
            rows = r0s
        if len(c0s)>1:
            step_y = min(c0s[i+1]-c0s[i] for i in range(len(c0s)-1))
            cols = list(range(c0s[0], m-w+1, step_y))
        else:
            cols = c0s
        have = {(c[0],c[1]) for c in cls if c[5]==mx}
        for x in rows:
            for y in cols:
                if (x,y) in have:
                    continue
                ok = True
                for i in range(h):
                    for j in range(w):
                        if mask[i][j] and grid[x+i][y+j]!=bg:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    for i in range(h):
                        for j in range(w):
                            if mask[i][j]:
                                out[x+i][y+j] = color
    return out