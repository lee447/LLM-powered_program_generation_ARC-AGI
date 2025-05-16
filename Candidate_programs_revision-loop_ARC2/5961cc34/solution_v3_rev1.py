from typing import List
from collections import deque
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    def comps(colors):
        vis = [[False]*w for _ in range(h)]
        res = []
        for i in range(h):
            for j in range(w):
                if not vis[i][j] and grid[i][j] in colors:
                    q = deque([(i,j)])
                    vis[i][j] = True
                    comp = [(i,j)]
                    while q:
                        x,y = q.popleft()
                        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx,ny = x+dx, y+dy
                            if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny] in colors:
                                vis[nx][ny] = True
                                q.append((nx,ny))
                                comp.append((nx,ny))
                    res.append(comp)
        return res
    ca = comps({1,3})
    group = ca if len(ca)>1 else comps({2,4})
    m = max(len(c) for c in group)
    res = [[8]*w for _ in range(h)]
    for c in group:
        if len(c)==m:
            for x,y in c:
                res[x][y] = 2
    return res