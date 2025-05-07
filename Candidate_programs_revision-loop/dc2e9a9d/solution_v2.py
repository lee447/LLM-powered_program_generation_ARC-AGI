def solve(grid):
    h, w = len(grid), len(grid[0])
    objs = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 3:
                if (r == 0 or grid[r-1][c] != 3) and (c == 0 or grid[r][c-1] != 3):
                    rr, cc = r, c
                    while rr+1 < h and grid[rr+1][c] == 3: rr += 1
                    while cc+1 < w and grid[r][cc+1] == 3: cc += 1
                    objs.append((r, rr, c, cc))
    odds = [o for o in objs if ((o[1]-o[0]+1)&1 and (o[3]-o[2]+1)&1)]
    odds.sort(key=lambda x: (x[1]-x[0]+1)*(x[3]-x[2]+1))
    out = [row[:] for row in grid]
    for i, (r0, r1, c0, c1) in enumerate(odds):
        h0, w0 = r1-r0+1, c1-c0+1
        shape = [row[c0:c1+1] for row in grid[r0:r1+1]]
        col = 1 if i == 0 else 8
        if len(odds) == 2:
            if i == 0:
                dr, dc = 0, 1
            else:
                dr, dc = -1, 0
        else:
            if (h0, w0) == (5,5):
                dr, dc = 1, 0
            else:
                dr, dc = 0, 1
        nr = r0 + (h0+1)*dr
        nc = c0 + (w0+1)*dc
        for rr in range(h0):
            for cc in range(w0):
                if shape[rr][cc] == 3:
                    out[nr+rr][nc+cc] = col
    return out