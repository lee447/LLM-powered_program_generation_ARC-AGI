from typing import List, Deque
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    res = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not vis[i][j]:
                q: Deque = deque()
                q.append((i,j))
                vis[i][j] = True
                comp = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==1:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                rs = [p[0] for p in comp]
                cs = [p[1] for p in comp]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                for x in range(r0, r1+1):
                    for y in range(c0, c1+1):
                        d = min(x-r0, r1-x, y-c0, c1-y)
                        if d==0:
                            res[x][y] = 2
                        elif d==1:
                            res[x][y] = 8
                        elif d==2:
                            res[x][y] = 6
    return res