import math
from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    q = deque()
    for i in range(h):
        for j in (0, w-1):
            if grid[i][j] != 5 and not visited[i][j]:
                visited[i][j] = True
                q.append((i, j))
    for j in range(w):
        for i in (0, h-1):
            if grid[i][j] != 5 and not visited[i][j]:
                visited[i][j] = True
                q.append((i, j))
    while q:
        i, j = q.popleft()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and grid[ni][nj] != 5:
                visited[ni][nj] = True
                q.append((ni, nj))
    holes = {(i,j) for i in range(h) for j in range(w) if not visited[i][j] and grid[i][j] in (0,4)}
    comps = []
    seen = set()
    for cell in holes:
        if cell in seen: continue
        comp = []
        dq = deque([cell])
        seen.add(cell)
        while dq:
            x, y = dq.popleft()
            comp.append((x, y))
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                if (nx, ny) in holes and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    dq.append((nx, ny))
        comps.append(comp)
    out = [row[:] for row in grid]
    for comp in comps:
        old4 = [p for p in comp if grid[p[0]][p[1]] == 4]
        if not old4: continue
        boundary = [p for p in comp if any((p[0]+di,p[1]+dj) not in comp for di,dj in ((1,0),(-1,0),(0,1),(0,-1)))]
        n = len(boundary)
        cx = sum(p[1] for p in boundary)/n
        cy = sum(p[0] for p in boundary)/n
        pts = []
        for i,j in boundary:
            angle = math.atan2(i-cy, j-cx)
            pts.append((angle, (i,j)))
        pts.sort()
        path = [p for _,p in pts]
        idxs = []
        for p in old4:
            idxs.append(path.index(p))
        new4 = [path[(i+1)%n] for i in idxs]
        for i,j in old4:
            out[i][j] = 0
        for i,j in new4:
            out[i][j] = 4
    return out