from collections import deque
def solve(grid):
    H, W = len(grid), len(grid[0])
    seen = [[False]*W for _ in range(H)]
    comps = []
    for r in range(H):
        for c in range(W):
            if grid[r][c]==3 and not seen[r][c]:
                q = deque([(r,c)])
                seen[r][c]=True
                comp = []
                while q:
                    x,y = q.popleft()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<H and 0<=ny<W and grid[nx][ny]==3 and not seen[nx][ny]:
                            seen[nx][ny]=True
                            q.append((nx,ny))
                comps.append(comp)
    rects = []
    for comp in comps:
        rs = [x for x,y in comp]
        cs = [y for x,y in comp]
        r0,r1 = min(rs), max(rs)
        c0,c1 = min(cs), max(cs)
        if r1-r0<2 or c1-c0<2: continue
        ok = True
        for cc in range(c0, c1+1):
            if (r0,cc) not in comp or (r1,cc) not in comp:
                ok = False; break
        if not ok: continue
        for rr in range(r0, r1+1):
            if (rr,c0) not in comp or (rr,c1) not in comp:
                ok = False; break
        if not ok: continue
        area = (r1-r0-1)*(c1-c0-1)
        if area>0:
            rects.append((area, r0, r1, c0, c1))
    if not rects:
        return grid
    m = min(a for a,_,_,_,_ in rects)
    out = [row[:] for row in grid]
    for a,r0,r1,c0,c1 in rects:
        if a==m:
            for i in range(r0+1, r1):
                for j in range(c0+1, c1):
                    if out[i][j]==0:
                        out[i][j]=3
    return out