from collections import deque, defaultdict

def solve(grid):
    h, w = len(grid), len(grid[0])
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
    for c, pts in comps:
        groups[c].append(pts)
    out = [[0]*w for _ in range(h)]
    for c, parts in sorted(groups.items(), key=lambda kv: (min(p[0] for p in kv[1][0]), min(p[1] for p in kv[1][0]))):
        if len(parts) == 1:
            for x,y in parts[0]:
                out[x][y] = c
        else:
            a, b = parts
            ax = sum(x for x,y in a)//len(a)
            ay = sum(y for x,y in a)//len(a)
            bx = sum(x for x,y in b)//len(b)
            by = sum(y for x,y in b)//len(b)
            dx, dy = bx-ax, by-ay
            steps = max(abs(dx), abs(dy))
            sx = 0 if dx==0 else dx//abs(dx)
            sy = 0 if dy==0 else dy//abs(dy)
            x, y = ax, ay
            for _ in range(steps+1):
                out[x][y] = c
                x += sx
                y += sy
    return out