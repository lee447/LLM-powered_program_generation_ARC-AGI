def solve(grid):
    H, W = len(grid), len(grid[0])
    original = [row[:] for row in grid]
    new = [row[:] for row in grid]
    seen = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            c = original[i][j]
            if c!=0 and not seen[i][j]:
                pts = [(i,j)]
                seen[i][j] = True
                qi = 0
                while qi < len(pts):
                    r,c0 = pts[qi]
                    qi += 1
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c0+dc
                        if 0<=rr<H and 0<=cc<W and not seen[rr][cc] and original[rr][cc]==c:
                            seen[rr][cc] = True
                            pts.append((rr,cc))
                comps.append((c, pts))
    # fill horizontal-only shapes
    for c, pts in comps:
        if len(pts) >= 3:
            rows = {r for r,_ in pts}
            cols = {co for _,co in pts}
            if len(rows)==1 and len(cols)>1:
                r0 = next(iter(rows))
                cs = sorted(co for _,co in pts)
                cmin, cmax = cs[0], cs[-1]
                # fill full horizontal
                for cc in range(cmin, cmax+1):
                    new[r0][cc] = c
                # find the gap column
                cg = None
                for cc in range(cmin, cmax+1):
                    if original[r0][cc] != c:
                        cg = cc
                        break
                if cg is not None:
                    # draw vertical up
                    for rr in range(r0):
                        if new[rr][cg] == 0:
                            new[rr][cg] = c
    # fill vertical-only shapes
    for c, pts in comps:
        if len(pts) >= 3:
            rows = {r for r,_ in pts}
            cols = {co for _,co in pts}
            if len(cols)==1 and len(rows)>1:
                c0 = next(iter(cols))
                rs = sorted(r for r,_ in pts)
                rmin, rmax = rs[0], rs[-1]
                # find the gap row
                rg = None
                for rr in range(rmin, rmax+1):
                    if original[rr][c0] != c:
                        rg = rr
                        break
                if rg is not None:
                    # fill only that cell
                    new[rg][c0] = c
    return new