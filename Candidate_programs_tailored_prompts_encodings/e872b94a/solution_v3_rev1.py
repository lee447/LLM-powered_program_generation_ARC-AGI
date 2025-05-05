from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not vis[i][j]:
                q = deque([(i,j)])
                vis[i][j] = True
                comp = []
                while q:
                    x,y = q.popleft()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==5:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                comps.append(comp)
    def max_run(coords, key_idx, other_idx):
        pts = {}
        for c in coords:
            k, o = c[key_idx], c[other_idx]
            pts.setdefault(k, []).append(o)
        best = 0
        for line in pts.values():
            line.sort()
            run = 1
            for i in range(1, len(line)):
                if line[i] == line[i-1] + 1:
                    run += 1
                else:
                    best = max(best, run)
                    run = 1
            best = max(best, run)
        return best
    count = 0
    for comp in comps:
        ln = len(comp)
        if ln == 4:
            if max_run(comp,1,0) >= 2:
                count += 1
            if max_run(comp,0,1) >= 2:
                count += 1
        elif ln >= 2:
            xs = {x for x,_ in comp}
            ys = {y for _,y in comp}
            if len(ys) == 1 and ln >= 2:
                count += 1
            elif len(xs) == 1 and ln >= 2:
                count += 1
            elif ln > 4:
                if max_run(comp,1,0) >= 2:
                    count += 1
    return [[0] for _ in range(count)]