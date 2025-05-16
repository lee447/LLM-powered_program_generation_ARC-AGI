from collections import deque
from math import atan2

def solve(grid):
    H, W = len(grid), len(grid[0])
    ctr = ((H-1)/2.0, (W-1)/2.0)
    visited = [[False]*W for _ in range(H)]
    comps = []
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v and not visited[r][c]:
                pts = []
                dq = deque([(r,c)])
                visited[r][c] = True
                while dq:
                    x,y = dq.popleft()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==v:
                            visited[nx][ny] = True
                            dq.append((nx,ny))
                sr = sum(x for x,y in pts)/len(pts)
                sc = sum(y for x,y in pts)/len(pts)
                ang = atan2(sr-ctr[0], sc-ctr[1])
                comps.append((ang, v, pts))
    comps.sort(key=lambda t: t[0])
    L = len(comps)
    res = [[0]*W for _ in range(H)]
    for i, (_, v, pts) in enumerate(comps):
        tgt = comps[(i+1)%L][2]
        for (r0,c0),(r1,c1) in zip(sorted(pts), sorted(tgt)):
            res[r1][c1] = v
    return res