def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] not in (0,5)]
    out = [[0]*w for _ in range(h)]
    for r,c,v in pts:
        out[r][c] = v
    if len(pts)==1:
        r,c,v = pts[0]
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        best = max(dirs, key=lambda d: (h if d[0] else w) - (r if d[0]<0 else h-1-r) if d[0] else (c if d[1]<0 else w-1-c))
        dr,dc = best
        steps = (r if dr<0 else h-1-r) if dr else (c if dc<0 else w-1-c)
        for i in range(1,steps):
            out[r+dr*i][c+dc*i] = 5
        out[r+dr*steps][c+dc*steps] = v
    else:
        for i,(r,c,v) in enumerate(pts):
            r2,c2,_ = pts[-1-i]
            dr = r2-r; dc = c2-c
            if abs(dr)>=abs(dc):
                sd = 1 if dr>0 else -1
                for i1 in range(abs(dr)):
                    out[r+sd*i1][c] = 5
                out[r+sd*abs(dr)][c] = v
            else:
                sd = 1 if dc>0 else -1
                for i1 in range(abs(dc)):
                    out[r][c+sd*i1] = 5
                out[r][c+sd*abs(dc)] = v
    return out