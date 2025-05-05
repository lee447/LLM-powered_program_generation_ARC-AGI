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
                for x, y in q:
                    pts.append((x, y))
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] == grid[i][j]:
                            seen[nx][ny] = True
                            q.append((nx, ny))
                rs = [p[0] for p in pts]
                cs = [p[1] for p in pts]
                comps.append((pts, min(rs), max(rs), min(cs), max(cs)))
    cr, cc = (h-1)/2, (w-1)/2
    frame = max(comps, key=lambda c: (c[2]-c[1]+1)*(c[4]-c[3]+1))
    _, fr0, fr1, fc0, fc1 = frame
    out = [row[:] for row in grid]
    for y in range(fc0+1, fc1):
        out[fr0][y] = 0
        out[fr1][y] = 0
    for x in range(fr0+1, fr1):
        out[x][fc0] = 0
        out[x][fc1] = 0
    for pts, r0, r1, c0, c1 in comps:
        if (pts, r0, r1, c0, c1) == frame:
            continue
        rr, cc_ = (r0+r1)/2, (c0+c1)/2
        val = grid[pts[0][0]][pts[0][1]]
        if rr < cr:
            x = r0 + 1
            if cc_ < cc:
                y0 = c1
                steps = fc0 - c1
                for k in range(1, steps+1):
                    out[x][y0+k] = val
            else:
                y0 = c0
                steps = c0 - fc1
                for k in range(1, steps+1):
                    out[x][y0-k] = val
        else:
            x0 = r0
            if cc_ < cc:
                y = c0 + 1
            else:
                y = c1 - 1
            steps = r0 - fr1
            for k in range(1, steps+1):
                out[x0-k][y] = val
    return out