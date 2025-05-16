from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    cnt = {}
    for i in range(n):
        for j in range(m):
            v = grid[i][j]
            if v:
                cnt[v] = cnt.get(v, 0) + 1
    if not cnt:
        return []
    main = max(cnt, key=cnt.get)
    seen = [[False]*m for _ in range(n)]
    best_comp = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == main and not seen[i][j]:
                comp = [(i,j)]
                seen[i][j] = True
                dq = deque([(i,j)])
                while dq:
                    x,y = dq.popleft()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<n and 0<=ny<m and not seen[nx][ny] and grid[nx][ny]==main:
                            seen[nx][ny] = True
                            comp.append((nx,ny))
                            dq.append((nx,ny))
                if len(comp) > len(best_comp):
                    best_comp = comp
    if not best_comp:
        return []
    minr = min(x for x,_ in best_comp)
    maxr = max(x for x,_ in best_comp)
    minc = min(y for _,y in best_comp)
    maxc = max(y for _,y in best_comp)
    h = maxr - minr + 1
    w = maxc - minc + 1
    s = max(h, w)
    dr = s - h
    dc = s - w
    maxr = min(n-1, maxr + dr)
    maxc = min(m-1, maxc + dc)
    return [row[minc:maxc+1] for row in grid[minr:maxr+1]]