from typing import List
from collections import deque
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bw = w // 3
    res = [[0]*3 for _ in range(3)]
    best = [[[0,0] for _ in range(3)] for _ in range(3)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for bx in range(3):
        vis = [[False]*bw for _ in range(h)]
        for y in range(h):
            for x in range(bw):
                if vis[y][x] or grid[y][bx*bw+x] == 0: continue
                c = grid[y][bx*bw+x]
                q = deque([(y,x)])
                vis[y][x] = True
                comp = []
                while q:
                    yy, xx = q.popleft()
                    comp.append((yy,xx))
                    for dy,dx in dirs:
                        ny, nx = yy+dy, xx+dx
                        if 0 <= ny < h and 0 <= nx < bw and not vis[ny][nx] and grid[ny][bx*bw+nx] == c:
                            vis[ny][nx] = True
                            q.append((ny,nx))
                sz = len(comp)
                if sz < 3: continue
                ys = [p[0] for p in comp]
                top, bot = min(ys), max(ys)
                r0 = int(top * 3 // h)
                r1 = int(bot * 3 // h)
                for ry in range(r0, r1+1):
                    if 0 <= ry < 3 and sz > best[ry][bx][0]:
                        best[ry][bx] = [sz, c]
    for ry in range(3):
        for bx in range(3):
            if best[ry][bx][0] > 0:
                res[ry][bx] = best[ry][bx][1]
    return res