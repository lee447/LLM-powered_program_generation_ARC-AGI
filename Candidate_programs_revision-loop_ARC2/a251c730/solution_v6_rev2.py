from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    frames = []
    for i in range(h):
        for j in range(w):
            if not vis[i][j]:
                c0 = grid[i][j]
                pts = []
                stack = [(i,j)]
                vis[i][j] = True
                while stack:
                    x,y = stack.pop()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not vis[nx][ny] and grid[nx][ny] == c0:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                if len(pts) < 4:
                    continue
                rs = [p[0] for p in pts]
                cs = [p[1] for p in pts]
                r0,r1 = min(rs), max(rs)
                c0_,c1 = min(cs), max(cs)
                hh, ww = r1-r0+1, c1-c0_+1
                per = 2*(hh+ww)-4
                if len(pts) != per:
                    continue
                ok = True
                for x,y in pts:
                    if not (x == r0 or x == r1 or y == c0_ or y == c1):
                        ok = False
                        break
                if ok:
                    frames.append((hh*ww, r0, r1, c0_, c1))
    if not frames:
        return grid
    _, r0, r1, c0, c1 = max(frames, key=lambda x: x[0])
    out = [row[c0:c1+1] for row in grid[r0:r1+1]]
    hh, ww = len(out), len(out[0])
    for i in range(hh):
        for j in range(ww):
            if i == 0 or i == hh-1 or j == 0 or j == ww-1:
                out[i][j] = 3
    return out