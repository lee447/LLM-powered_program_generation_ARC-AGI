import numpy as np

def solve(grid):
    h, w = len(grid), len(grid[0])
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    def bands_of_2(g):
        bs = []
        inb = False
        for r in range(h):
            if any(g[r][c]==2 for c in range(w)):
                if not inb:
                    start = r
                    inb = True
            else:
                if inb:
                    bs.append((start, r-1))
                    inb = False
        if inb:
            bs.append((start, h-1))
        return bs

    def components(r0, r1):
        seen = [[False]*w for _ in range(h)]
        comps = []
        for r in range(r0, r1+1):
            for c in range(w):
                if grid[r][c]==2 and not seen[r][c]:
                    stack = [(r,c)]
                    seen[r][c] = True
                    comp = []
                    while stack:
                        x,y = stack.pop()
                        comp.append((x,y))
                        for d in range(4):
                            nx, ny = x+dr[d], y+dc[d]
                            if r0<=nx<=r1 and 0<=ny<w and grid[nx][ny]==2 and not seen[nx][ny]:
                                seen[nx][ny] = True
                                stack.append((nx,ny))
                    comps.append(comp)
        return comps

    def sig(comp):
        xs = [x for x,_ in comp]
        ys = [y for _,y in comp]
        minx, miny = min(xs), min(ys)
        pts = sorted(((x-minx, y-miny) for x,y in comp))
        return tuple(pts)

    out = [row[:] for row in grid]
    seen_same = {}
    for bi,(r0,r1) in enumerate(bands_of_2(grid)):
        comps = components(r0, r1)
        if len(comps)!=2:
            continue
        c0, c1 = comps
        s0, s1 = sig(c0), sig(c1)
        left, right = (c0, c1) if np.mean([y for _,y in c0])<np.mean([y for _,y in c1]) else (c1, c0)
        sl, sr = sig(left), sig(right)
        if sl!=sr:
            for x,y in left:
                out[x][y] = 8
            for x,y in right:
                out[x][y] = 3
        else:
            cnt = seen_same.get(sl,0)
            if cnt==0:
                side = 'right' if any(grid[x][y]==2 for x,y in right) else 'right'
                col = 8 if cnt==0 else 3
                if side=='left':
                    for x,y in left: out[x][y]=col
                else:
                    for x,y in right: out[x][y]=col
            elif cnt==1:
                col = 3
                for x,y in right: out[x][y]=col
            seen_same[sl] = cnt+1
    return out