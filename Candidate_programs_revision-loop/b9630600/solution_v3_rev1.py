from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    comp_id = [[-1]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    comps = {}
    cid = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and comp_id[i][j] < 0:
                color = grid[i][j]
                q = deque([(i,j)])
                comp_id[i][j] = cid
                pts = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]==color and comp_id[nx][ny]<0:
                            comp_id[nx][ny] = cid
                            q.append((nx,ny))
                            pts.append((nx,ny))
                comps[cid] = (color, pts)
                cid += 1
    outside_zero = [[False]*w for _ in range(h)]
    q = deque()
    for i in range(h):
        for j in (0, w-1):
            if grid[i][j] == 0 and not outside_zero[i][j]:
                outside_zero[i][j] = True
                q.append((i,j))
    for j in range(w):
        for i in (0, h-1):
            if grid[i][j] == 0 and not outside_zero[i][j]:
                outside_zero[i][j] = True
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            if 0<=nx<h and 0<=ny<w and grid[nx][ny]==0 and not outside_zero[nx][ny]:
                outside_zero[nx][ny] = True
                q.append((nx,ny))
    out = [row[:] for row in grid]
    for cid, (color, pts) in comps.items():
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        x0,x1,y0,y1 = min(xs), max(xs), min(ys), max(ys)
        holes = []
        for i in range(x0, x1+1):
            for j in range(y0, y1+1):
                if grid[i][j]==0 and not outside_zero[i][j]:
                    holes.append((i,j))
        if holes:
            for i,j in holes:
                out[i][j] = color
        else:
            s = set(pts)
            for x,y in pts:
                cnt = 0
                for dx,dy in dirs:
                    if (x+dx,y+dy) in s:
                        cnt +=1
                if cnt==4:
                    out[x][y] = 0
    return out