def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [[0]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for r in range(h):
        for c in range(w):
            if grid[r][c] in (1,2,3,6):
                res[r][c] = grid[r][c]
    for color in (1,2,3,6):
        pts = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==color]
        if not pts: continue
        (r1,c1) = pts[0]
        if len(pts)>1:
            (r2,c2) = pts[1]
        else:
            if r1 < h//2:
                r2 = r1 + (h//2 - r1)
            else:
                r2 = r1 - (r1 - h//2)
            if c1 < w//2:
                c2 = c1 + (w//2 - c1)
            else:
                c2 = c1 - (c1 - w//2)
        res[r2][c2] = color
        if r1==r2:
            for cc in range(min(c1,c2)+1, max(c1,c2)):
                res[r1][cc]=5
        elif c1==c2:
            for rr in range(min(r1,r2)+1, max(r1,r2)):
                res[rr][c1]=5
        else:
            br, bc = r1, c2
            best = (abs(br-r2)+abs(bc-c2)+abs(br-r1)+abs(bc-c1), br, bc)
            br2, bc2 = r2, c1
            cand = (abs(br2-r2)+abs(bc2-c2)+abs(br2-r1)+abs(bc2-c1), br2, bc2)
            if cand<best: best=(cand[0], br2, bc2)
            bend_r, bend_c = best[1], best[2]
            for rr in range(min(r1,bend_r)+1, max(r1,bend_r)):
                res[rr][c1]=5
            for cc in range(min(c1,bend_c)+1, max(c1,bend_c)):
                res[bend_r][cc]=5
            for rr in range(min(r2,bend_r)+1, max(r2,bend_r)):
                res[rr][c2]=5
            for cc in range(min(c2,bend_c)+1, max(c2,bend_c)):
                res[bend_r][cc]=5
            res[bend_r][bend_c]=4
    return res