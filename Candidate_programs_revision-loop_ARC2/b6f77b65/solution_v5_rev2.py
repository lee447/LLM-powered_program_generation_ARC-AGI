from collections import deque
import math

def solve(grid):
    H, W = len(grid), len(grid[0])
    center_r, center_c = (H-1)/2.0, (W-1)/2.0
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
                ang = math.atan2(sr-center_r, sc-center_c)
                comps.append((ang, v, pts))
    comps.sort(key=lambda t: t[0])
    n = len(comps)
    res = [[0]*W for _ in range(H)]
    if n:
        _, v0, pts0 = comps[0]
        for r,c in pts0:
            res[r][c] = v0
        for i in range(1, n):
            v_prev = comps[i-1][1]
            for r,c in comps[i][2]:
                res[r][c] = v_prev
    return res