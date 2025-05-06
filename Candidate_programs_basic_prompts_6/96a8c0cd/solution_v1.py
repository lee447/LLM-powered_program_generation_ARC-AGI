def solve(grid):
    from collections import deque
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    used = [[False]*w for _ in range(h)]
    comps = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] not in (0,2) and not used[y][x]:
                c = grid[y][x]
                q = [(y,x)]
                used[y][x] = True
                comp = [(y,x)]
                for yy,xx in q:
                    for dy,dx in dirs:
                        ny, nx = yy+dy, xx+dx
                        if 0<=ny<h and 0<=nx<w and not used[ny][nx] and grid[ny][nx]==c:
                            used[ny][nx] = True
                            q.append((ny,nx))
                            comp.append((ny,nx))
                if len(comp)>1:
                    comps.append(comp)
    points = []
    for comp in comps:
        ys = [p[0] for p in comp]
        xs = [p[1] for p in comp]
        y1,y2,minx,maxx = min(ys), max(ys), min(xs), max(xs)
        if y1==y2:
            r = y1
            if minx-1>=0:
                ent = (r, minx-1); ext = (r, maxx+1)
            else:
                ent = (r, maxx+1); ext = (r, minx-1)
            points.append(ent); points.append(ext)
        else:
            c0 = (y1+y2)//2
            if minx-1>=0:
                ent = (c0, minx-1)
            elif maxx+1<w:
                ent = (c0, maxx+1)
            elif y1-1>=0:
                ent = (y1-1, minx)
            else:
                ent = (y2+1, minx)
            points.append(ent)
    points = sorted(points)
    twos = [(y,x) for y in range(h) for x in range(w) if grid[y][x]==2]
    if twos:
        cur = twos[0]
    else:
        cur = points.pop(0)
    def bfs(s, t):
        q = deque([s])
        prev = {s:None}
        while q:
            y,x = q.popleft()
            if (y,x)==t:
                p = []
                while (y,x) is not None:
                    p.append((y,x))
                    y,x = prev[(y,x)] if prev[(y,x)] is not None else (None,None)
                return p[::-1]
            for dy,dx in dirs:
                ny, nx = y+dy, x+dx
                if 0<=ny<h and 0<=nx<w and (ny,nx) not in prev:
                    if (ny,nx)==t or grid[ny][nx]==0:
                        prev[(ny,nx)] = (y,x)
                        q.append((ny,nx))
        return []
    for p in points:
        path = bfs(cur, p)
        for y,x in path:
            if grid[y][x]==0:
                grid[y][x] = 2
        cur = p
    return grid