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
    all_comps = []
    for colors in ({1,3},{2,4}):
        for c in comps(colors):
            cols = {grid[x][y] for x,y in c}
            if len(cols) > 1:
                all_comps.append(c)
    if not all_comps:
        return [[8]*w for _ in range(h)]
    target = max(all_comps, key=len)
    min_i = min(x for x,_ in target)
    max_i = max(x for x,_ in target)
    min_j = min(y for _,y in target)
    max_j = max(y for _,y in target)
    width = max_j - min_j + 1
    height = max_i - min_i + 1
    res = [[8]*w for _ in range(h)]
    if width == 1:
        for i in range(h):
            res[i][min_j] = 2
    elif height == 1:
        for j in range(w):
            res[min_i][j] = 2
    else:
        for i in range(min_i, max_i+1):
            for j in range(min_j, max_j+1):
                res[i][j] = 2
    return res