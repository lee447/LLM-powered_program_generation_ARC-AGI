def solve(grid):
    from collections import deque
    h, w = len(grid), len(grid[0])
    seeds = [(x,y) for y in range(h) for x in range(w) if grid[y][x]==6]
    seen = [[False]*w for _ in range(h)]
    clusters = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for y in range(h):
        for x in range(w):
            if grid[y][x]==2 and not seen[y][x]:
                q=deque([(x,y)]); seen[y][x]=True; pts=[(x,y)]
                while q:
                    cx,cy=q.popleft()
                    for dx,dy in dirs:
                        nx,ny=cx+dx,cy+dy
                        if 0<=nx<w and 0<=ny<h and not seen[ny][nx] and grid[ny][nx]==2:
                            seen[ny][nx]=True; q.append((nx,ny)); pts.append((nx,ny))
                sx = sum(px for px,py in pts)//len(pts)
                sy = sum(py for px,py in pts)//len(pts)
                clusters.append((sx,sy))
    terms = list({p for p in seeds+clusters})
    n = len(terms)
    parent = list(range(n))
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]
            a=parent[a]
        return a
    def union(a,b):
        ra,rb = find(a),find(b)
        if ra==rb: return False
        parent[rb]=ra
        return True
    edges = []
    for i in range(n):
        x1,y1=terms[i]
        for j in range(i+1,n):
            x2,y2=terms[j]
            edges.append((abs(x1-x2)+abs(y1-y2),i,j))
    edges.sort()
    for _,i,j in edges:
        if union(i,j):
            x1,y1 = terms[i]
            x2,y2 = terms[j]
            dy = 1 if y2>y1 else -1
            for yy in range(y1, y2+dy, dy):
                if grid[yy][x1]==7: grid[yy][x1]=6
            dx = 1 if x2>x1 else -1
            for xx in range(x1, x2+dx, dx):
                if grid[y2][xx]==7: grid[y2][xx]=6
    return grid