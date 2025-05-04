def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import defaultdict
    comps = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c == 0: continue
            if c not in comps: comps[c] = [i, i, j, j]
            else:
                comps[c][0] = min(comps[c][0], i)
                comps[c][1] = max(comps[c][1], i)
                comps[c][2] = min(comps[c][2], j)
                comps[c][3] = max(comps[c][3], j)
    rects = {}
    for c,(r0,r1,c0,c1) in comps.items():
        ok = True
        for i in range(r0, r1+1):
            for j in range(c0, c1+1):
                if grid[i][j] != c:
                    ok = False; break
            if not ok: break
        if ok:
            rects[c] = (r0,r1,c0,c1)
    pairs = sorted(rects.items(), key=lambda x:(x[1][1]-x[1][0]+1)*(x[1][3]-x[1][2]+1))
    if len(pairs) < 2: return grid
    (c1, (r01,r11,c01,c11)), (c2, (r02,r12,c02,c12)) = pairs[0], pairs[1]
    h1, w1 = r11-r01+1, c11-c01+1
    h2, w2 = r12-r02+1, c12-c02+1
    if h1*h1 == h2*h2 and h1 == h2 and w1 == w2:
        new = [row[:] for row in grid]
        for di in range(h1):
            for dj in range(w1):
                new[r01+di][c01+dj] = grid[r02+di][c02+dj]
                new[r02+di][c02+dj] = grid[r01+di][c01+dj]
        return new
    return grid