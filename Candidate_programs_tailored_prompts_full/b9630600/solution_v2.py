def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                q = [(i,j)]
                seen[i][j] = True
                pts = []
                for x,y in q:
                    pts.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]!=0 and not seen[nx][ny]:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                rs = [p[0] for p in pts]
                cs = [p[1] for p in pts]
                comps.append((pts, min(rs), max(rs), min(cs), max(cs)))
    cr = (h-1)/2
    cc = (w-1)/2
    best = None
    bestd = None
    for c in comps:
        r0,r1,c0,c1 = c[1],c[2],c[3],c[4]
        rr,ccn = (r0+r1)/2,(c0+c1)/2
        d = (rr-cr)**2+(ccn-cc)**2
        if bestd is None or d<bestd:
            bestd = d
            best = c
    center, r0, r1, c0, c1 = best
    B = (c1-c0+1)-2
    out = [row[:] for row in grid]
    for y in range(c0+1,c1):
        out[r0][y] = 0
        out[r1][y] = 0
    for x in range(r0+1,r1):
        out[x][c0] = 0
        out[x][c1] = 0
    for c in comps:
        if c is best: continue
        pts,r0_,r1_,c0_,c1_ = c
        rr = (r0_+r1_)/2
        cc_ = (c0_+c1_)/2
        if rr<cr and cc_<cc:
            x,y = r0_+1, c1_
            for k in range(1,B+1):
                out[x][y+k] = grid[x][y]
        elif rr<cr and cc_>cc:
            x,y = r0_+1, c0_
            for k in range(1,B+1):
                out[x][y-k] = grid[x][y]
        elif rr>cr and cc_<cc:
            x,y = r0_, c0_+1
            for k in range(1,B+1):
                out[x+k][y] = grid[x][y]
        else:
            x,y = r0_, c0_-1
            for k in range(1,B+1):
                out[x-k][y] = grid[x][y]
    return out