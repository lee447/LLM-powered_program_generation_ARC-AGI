from typing import List
from collections import deque, Counter

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] > 1 and not vis[i][j]:
                c = grid[i][j]
                q = deque([(i,j)])
                comp = [(i,j)]
                vis[i][j] = True
                while q:
                    x,y = q.popleft()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny] = True
                            comp.append((nx,ny))
                            q.append((nx,ny))
                shapes.append((len(comp), c, set(comp)))
    if not shapes:
        return grid
    _, fc, frame = max(shapes)
    reach = [[False]*w for _ in range(h)]
    q = deque()
    for i in range(h):
        for j in (0, w-1):
            if (i,j) not in frame:
                reach[i][j] = True
                q.append((i,j))
    for j in range(w):
        for i in (0, h-1):
            if (i,j) not in frame and not reach[i][j]:
                reach[i][j] = True
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx, y+dy
            if 0<=nx<h and 0<=ny<w and not reach[nx][ny] and (nx,ny) not in frame:
                reach[nx][ny] = True
                q.append((nx,ny))
    interior = []
    for i in range(h):
        for j in range(w):
            if (i,j) not in frame and not reach[i][j]:
                interior.append((i,j))
    if interior:
        nbr = []
        for x,y in interior:
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny = x+dx, y+dy
                if 0<=nx<h and 0<=ny<w and reach[nx][ny]:
                    nbr.append(grid[nx][ny])
        fill = 1
        if nbr:
            fill = Counter(nbr).most_common(1)[0][0]
        res = [row[:] for row in grid]
        for x,y in interior:
            res[x][y] = fill
        return res
    return [row[:] for row in grid]