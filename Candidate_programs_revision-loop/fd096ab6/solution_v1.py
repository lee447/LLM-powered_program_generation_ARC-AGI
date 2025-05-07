def solve(grid):
    h, w = len(grid), len(grid[0])
    shapeA = [(0,2),(0,3),(1,0),(1,1),(2,2)]
    shapeB = [(0,1),(0,2),(1,0),(1,1),(2,1)]
    shapes = [shapeA, shapeB]
    out = [row[:] for row in grid]
    clusters = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != 1:
                clusters.setdefault(c, []).append((i,j))
    for c, pts in clusters.items():
        for rel in shapes:
            rh = max(r for r,_ in rel) + 1
            rw = max(c0 for _,c0 in rel) + 1
            found = False
            for oi in range(h - rh + 1):
                if found: break
                for oj in range(w - rw + 1):
                    ok = True
                    for pi,pj in pts:
                        dr, dc = pi - oi, pj - oj
                        if (dr,dc) not in rel:
                            ok = False
                            break
                    if ok:
                        for dr,dc in rel:
                            out[oi+dr][oj+dc] = c
                        found = True
                        break
                if found: break
            if found: break
    return out