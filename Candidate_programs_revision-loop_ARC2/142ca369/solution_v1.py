def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import deque, defaultdict
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c and not vis[i][j]:
                q = deque([(i,j)])
                vis[i][j] = True
                pts = []
                while q:
                    x,y = q.popleft()
                    pts.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                comps.append((c, pts))
    groups = defaultdict(list)
    for c,pts in comps:
        groups[c].append(pts)
    items = sorted(groups.items(), key=lambda kv: (min(p[0] for p in kv[1][0]), min(p[1] for p in kv[1][0])))
    out = [[0]*w for _ in range(h)]
    for c, (a,b) in items:
        if len(groups[c])==1:
            pts1 = a
            pts2 = a
        else:
            pts1, pts2 = groups[c]
        ax = sum(x for x,y in pts1)//len(pts1)
        ay = sum(y for x,y in pts1)//len(pts1)
        bx = sum(x for x,y in pts2)//len(pts2)
        by = sum(y for x,y in pts2)//len(pts2)
        dx = bx - ax
        dy = by - ay
        steps = max(abs(dx), abs(dy))
        sx = 0 if dx==0 else dx//abs(dx)
        sy = 0 if dy==0 else dy//abs(dy)
        curx, cury = ax, ay
        for _ in range(steps+1):
            for x,y in pts1:
                rx = x - ax + curx
                ry = y - ay + cury
                if 0<=rx<h and 0<=ry<w:
                    out[rx][ry] = c
            curx += sx
            cury += sy
    return out