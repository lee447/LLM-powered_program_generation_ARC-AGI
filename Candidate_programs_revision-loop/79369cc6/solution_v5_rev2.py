from typing import List
from collections import deque
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==6 and not vis[i][j]:
                q = deque([(i,j)])
                vis[i][j] = True
                comp = [(i,j)]
                while q:
                    y,x = q.popleft()
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx]==6:
                            vis[ny][nx] = True
                            q.append((ny,nx))
                            comp.append((ny,nx))
                if len(comp)==2:
                    comps.append(comp)
    g = [row[:] for row in grid]
    for comp in comps:
        (r0,c0),(r1,c1) = comp
        dr,dc = r1-r0, c1-c0
        v1 = (dr//abs(dr) if dr else 0, dc//abs(dc) if dc else 0)
        v2 = (-v1[0], -v1[1])
        def countv(v):
            return sum(1 for j in range(1,3) if 0<=comp_base[0]+v[0]*j<h and 0<=comp_base[1]+v[1]*j<w and grid[comp_base[0]+v[0]*j][comp_base[1]+v[1]*j]==0)
        # pick v
        # temporary base choose first; adjust after pick v
        comp_base = comp[0]
        c1v = countv(v1)
        comp_base = comp[0]
        c2v = countv(v2)
        v = v1 if c1v>=c2v else v2
        # choose base along v
        comp_base = min(comp, key=lambda c: c[0]*v[0]+c[1]*v[1])
        # perpendicular
        p1 = (-v[1], v[0])
        p2 = (v[1], -v[0])
        l = len(comp) + 1
        def valid_p(p):
            y = comp_base[0] + p[0]*l
            x = comp_base[1] + p[1]*l
            return 0<=y<h and 0<=x<w
        vp = p1 if valid_p(p1) and not valid_p(p2) else (p2 if valid_p(p2) and not valid_p(p1) else p2)
        if valid_p(p1) and valid_p(p2):
            c1p = sum(1 for i in range(1,l+1) if 0<=comp_base[0]+p1[0]*i<h and 0<=comp_base[1]+p1[1]*i<w and grid[comp_base[0]+p1[0]*i][comp_base[1]+p1[1]*i]==0)
            c2p = sum(1 for i in range(1,l+1) if 0<=comp_base[0]+p2[0]*i<h and 0<=comp_base[1]+p2[1]*i<w and grid[comp_base[0]+p2[0]*i][comp_base[1]+p2[1]*i]==0)
            vp = p1 if c1p>c2p else p2
        pd = vp
        for i in range(l+1):
            jmax = min(len(comp), l - i)
            for j in range(jmax+1):
                if i==0 and j==0: continue
                y = comp_base[0] + pd[0]*i + v[0]*j
                x = comp_base[1] + pd[1]*i + v[1]*j
                if 0<=y<h and 0<=x<w and grid[y][x]==0:
                    g[y][x] = 4
    return g