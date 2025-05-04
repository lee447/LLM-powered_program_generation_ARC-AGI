from typing import List
from collections import deque
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    seen = [[False]*m for _ in range(n)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    bar = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 5 and not seen[i][j]:
                dq = deque([(i,j)])
                seen[i][j] = True
                comp = []
                while dq:
                    x,y = dq.popleft()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m and not seen[nx][ny] and grid[nx][ny] == 5:
                            seen[nx][ny] = True
                            dq.append((nx,ny))
                bar = comp
    rs = [r for r,c in bar]; cs = [c for r,c in bar]
    rmin, rmax, cmin, cmax = min(rs), max(rs), min(cs), max(cs)
    orient = 'v' if cmin == cmax else 'h'
    if orient == 'v':
        right = sum(1 for r,c in bar if c+1 < m and grid[r][c+1] not in (0,5))
        left = sum(1 for r,c in bar if c-1 >= 0 and grid[r][c-1] not in (0,5))
        side = 'right' if right > left else 'left'
        init = []
        for r,c in bar:
            nc = c+1 if side=='right' else c-1
            if 0 <= nc < m and grid[r][nc] not in (0,5):
                init.append((r,nc))
    else:
        down = sum(1 for r,c in bar if r+1 < n and grid[r+1][c] not in (0,5))
        up = sum(1 for r,c in bar if r-1 >= 0 and grid[r-1][c] not in (0,5))
        side = 'down' if down > up else 'up'
        init = []
        for r,c in bar:
            nr = r+1 if side=='down' else r-1
            if 0 <= nr < n and grid[nr][c] not in (0,5):
                init.append((nr,c))
    pq = set()
    dq = deque(init)
    while dq:
        x,y = dq.popleft()
        if (x,y) in pq: continue
        if grid[x][y] in (0,5): continue
        pq.add((x,y))
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and (nx,ny) not in pq and grid[nx][ny] not in (0,5):
                dq.append((nx,ny))
    prs = [r for r,c in pq]; pcs = [c for r,c in pq]
    prmin, prmax, pcmin, pcmax = min(prs), max(prs), min(pcs), max(pcs)
    ph, pw = prmax-prmin+1, pcmax-pcmin+1
    pat = [grid[r][pcmin:pcmax+1] for r in range(prmin, prmax+1)]
    if orient == 'v':
        if side == 'right':
            sc = cmax+1
        else:
            sc = cmin-pw
        for i in range(rmin, rmax+1):
            for j in range(sc, sc+pw):
                res[i][j] = pat[(i-rmin)%ph][(j-sc)%pw]
    else:
        if side == 'down':
            sr = rmax+1
        else:
            sr = rmin-ph
        for i in range(sr, sr+ph):
            for j in range(cmin, cmax+1):
                res[i][j] = pat[(i-sr)%ph][(j-cmin)%pw]
    return res