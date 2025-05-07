def solve(grid):
    H = len(grid)
    W = len(grid[0])
    pts = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0:
                pts.append((r, c, grid[r][c]))
    out = [row[:] for row in grid]
    def sign(x):
        return (x>0) - (x<0)
    used = [[False]*W for _ in range(H)]
    for r,c,_ in pts:
        used[r][c] = True
    n = len(pts)
    for i in range(n):
        r, c, v = pts[i]
        rt, ct, _ = pts[(i+1)%n]
        C = (r, ct)
        D = (rt, c)
        paths = []
        for corner in (C, D):
            dr = corner[0] - r
            dc = corner[1] - c
            length = abs(dr) + abs(dc)
            pts_line = []
            if dr != 0:
                step = sign(dr)
                for rr in range(r+step, corner[0]+step, step):
                    pts_line.append((rr, c))
            if dc != 0:
                step = sign(dc)
                for cc in range(c+step, corner[1]+step, step):
                    pts_line.append((corner[0], cc))
            paths.append((length, pts_line, corner))
        paths.sort(key=lambda x: x[0])
        length, seg, corner = paths[0]
        for (rr, cc) in seg:
            if not used[rr][cc]:
                out[rr][cc] = 5
                used[rr][cc] = True
        dr = corner[0] - r
        dc = corner[1] - c
        if dr != 0 and dc == 0:
            ext_dirs = [(sign(dr),0),(0,sign(ct-c)),(0,-sign(ct-c))]
        elif dc != 0 and dr == 0:
            ext_dirs = [(0,sign(dc)),(sign(rt-r),0),(-sign(rt-r),0)]
        else:
            ext_dirs = [(sign(dr),sign(dc)),(-sign(dr),-sign(dc))]
        placed = False
        for ed in ext_dirs:
            rr = corner[0] + ed[0]
            cc = corner[1] + ed[1]
            if 0 <= rr < H and 0 <= cc < W and not used[rr][cc]:
                out[rr][cc] = v
                used[rr][cc] = True
                placed = True
                break
    return out