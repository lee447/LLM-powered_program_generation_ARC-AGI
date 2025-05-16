from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    comps = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c not in (1, 8) and not vis[i][j]:
                stack = [(i,j)]
                comp = []
                vis[i][j] = True
                while stack:
                    x,y = stack.pop()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and grid[nx][ny] == c:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                comps.setdefault(c, []).append(comp)
    for color, clist in comps.items():
        if len(clist) != 2:
            continue
        set1 = set(clist[0])
        set2 = set(clist[1])
        dq = deque()
        prev = {}
        seen = set()
        for p in set1:
            dq.append(p)
            seen.add(p)
        end = None
        while dq and end is None:
            x,y = dq.popleft()
            if (x,y) in set2:
                end = (x,y)
                break
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny = x+dx, y+dy
                if 0 <= nx < h and 0 <= ny < w and (nx,ny) not in seen:
                    v = grid[nx][ny]
                    if v == 8 or (nx,ny) in set1 or (nx,ny) in set2:
                        seen.add((nx,ny))
                        prev[(nx,ny)] = (x,y)
                        dq.append((nx,ny))
        if end is None:
            continue
        cur = end
        while cur not in set1:
            x,y = cur
            if out[x][y] == 8:
                out[x][y] = color
            cur = prev[cur]
    return out