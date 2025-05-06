def solve(grid):
    h, w = len(grid), len(grid[0])
    pts = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0]
    if not pts:
        return grid
    pts.sort(key=lambda x: x[2])
    out = [[0]*w for _ in range(h)]
    for r,c,v in pts:
        out[r][c] = v
    def line(a, b, col, mark):
        (r1,c1,_),(r2,c2,_) = a,b
        er, ec = r2, c1
        dr = 1 if er>r1 else -1 if er<r1 else 0
        for r in range(r1+dr, er+dr, dr):
            if (r,c1)!=(r2,c2) and (r,c1)!=(r1,c1):
                out[r][c1] = col
        dc = 1 if c2>c1 else -1 if c2<c1 else 0
        for c in range(c1+dc, c2+dc, dc):
            if (er,c)!=(r2,c2) and (er,c)!=(r1,c1):
                out[er][c] = col
        out[er][ec] = mark
        # reflect endpoints
        for (r0,c0,v0) in (a,b):
            rr, cc = 2*er-r0, 2*ec-c0
            if 0<=rr<h and 0<=cc<w:
                out[rr][cc] = v0
        # extend mark
        drx = 1 if er>r1 else -1 if er<r1 else 0
        dcx = 1 if ec>c1 else -1 if ec<c1 else 0
        rr,cc = er+drx, ec+dcx
        while 0<=rr<h and 0<=cc<w and out[rr][cc]==0:
            out[rr][cc] = mark
            rr += drx; cc += dcx

    if len(pts)==1:
        a = pts[0]
        b = pts[0]
        line(a,b,5,a[2])
    else:
        for i in range(len(pts)-1):
            line(pts[i], pts[i+1], 5, 4)
    return out