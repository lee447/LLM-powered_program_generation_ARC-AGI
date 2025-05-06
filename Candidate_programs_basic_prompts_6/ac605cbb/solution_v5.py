def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [[grid[r][c] for c in range(w)] for r in range(h)]
    pts = [(r, c, grid[r][c]) for r in range(h) for c in range(w) if grid[r][c] != 0]
    def sign(x): return (x > 0) - (x < 0)
    if len(pts) == 1:
        r, c, v = pts[0]
        qr = h - 1 - r
        for i in range(min(r, qr) + 1, max(r, qr)):
            out[i][c] = 5
        out[qr][c] = v
    elif len(pts) == 2:
        (r0, c0, v0), (r1, c1, v1) = pts
        dr, dc = r1 - r0, c1 - c0
        if abs(dr) > abs(dc):
            q0 = (r0 - sign(dr), c0 + sign(dc) * abs(dc))
            q1 = (r1, c1 - sign(dc) * abs(dc))
            # path for first
            rr, cc = r0, c0
            tr, tc = q0
            sr, sc = sign(tr - rr), 0
            for _ in range(abs(tr - rr)):
                rr += sr
                out[rr][cc] = 5
            sr, sc = 0, sign(tc - cc)
            for _ in range(abs(tc - cc)):
                cc += sc
                out[rr][cc] = 5
            out[tr][tc] = v0
            # path for second
            rr, cc = r1, c1
            tr, tc = q1
            sr, sc = 0, sign(tc - cc)
            for _ in range(abs(tc - cc)):
                cc += sc
                out[rr][cc] = 5
            sr, sc = sign(tr - rr), 0
            for _ in range(abs(tr - rr)):
                rr += sr
                out[rr][cc] = 5
            out[tr][tc] = v1
            # intersection
            ir, ic = q0[0], q1[1]
            if 0 <= ir < h and 0 <= ic < w and out[ir][ic] == 5:
                out[ir][ic] = 4
                drd, dcd = sign(pt := pts[1][0] - ir), sign(pts[0][1] - ic)
                r2, c2 = ir, ic
                while True:
                    nr, nc = r2 + drd, c2 + dcd
                    if 0 <= nr < h and 0 <= nc < w and out[nr][nc] == 0:
                        out[nr][nc] = 4
                        r2, c2 = nr, nc
                    else:
                        break
        else:
            q0 = (r0 + sign(dr) * abs(dr), c0 - sign(dc))
            q1 = (r1 - sign(dr) * abs(dr), c1 + sign(dc))
            # path for first
            rr, cc = r0, c0
            tr, tc = q0
            sr, sc = 0, sign(tc - cc)
            for _ in range(abs(tc - cc)):
                cc += sc
                out[rr][cc] = 5
            sr, sc = sign(tr - rr), 0
            for _ in range(abs(tr - rr)):
                rr += sr
                out[rr][cc] = 5
            out[tr][tc] = v0
            # path for second
            rr, cc = r1, c1
            tr, tc = q1
            sr, sc = sign(tr - rr), 0
            for _ in range(abs(tr - rr)):
                rr += sr
                out[rr][cc] = 5
            sr, sc = 0, sign(tc - cc)
            for _ in range(abs(tc - cc)):
                cc += sc
                out[rr][cc] = 5
            out[tr][tc] = v1
            # intersection
            ir, ic = q1[0], q0[1]
            if 0 <= ir < h and 0 <= ic < w and out[ir][ic] == 5:
                out[ir][ic] = 4
                drd, dcd = sign(pt := pts[0][0] - ir), sign(pts[1][1] - ic)
                r2, c2 = ir, ic
                while True:
                    nr, nc = r2 + drd, c2 + dcd
                    if 0 <= nr < h and 0 <= nc < w and out[nr][nc] == 0:
                        out[nr][nc] = 4
                        r2, c2 = nr, nc
                    else:
                        break
    else:
        # multiple points: do each as one-point rule
        for r, c, v in pts:
            qr = h - 1 - r
            for i in range(min(r, qr) + 1, max(r, qr)):
                out[i][c] = 5
            out[qr][c] = v
    return out