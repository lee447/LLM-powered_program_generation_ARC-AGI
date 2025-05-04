def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                col6 = False
                pts = [(i,j)]
                seen[i][j] = True
                if grid[i][j] == 6: col6 = True
                for k in range(len(pts)):
                    y,x = pts[k]
                    for dy,dx in dirs:
                        ny,nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and grid[ny][nx]!=0 and not seen[ny][nx]:
                            seen[ny][nx] = True
                            pts.append((ny,nx))
                            if grid[ny][nx] == 6: col6 = True
                if col6:
                    ys = [p[0] for p in pts]
                    xs = [p[1] for p in pts]
                    comps.append((len(set(pts)), min(ys), max(ys), min(xs), max(xs)))
    comps.sort()
    _, y0, y1, x0, x1 = comps[0]
    sub = [row[x0:x1+1] for row in grid[y0:y1+1]]
    hh, ww = len(sub), len(sub[0])
    out = []
    half = (hh+1)//2
    for i in range(half):
        top = sub[i]
        bot = sub[hh-1-i]
        m0 = [c!=0 for c in top]
        m1 = [c!=0 for c in bot]
        if sum(m0)==ww and i==0:
            m = [False]*ww
            m[0] = m[-1] = True
        else:
            m = [m0[j] or m1[j] for j in range(ww)]
            if sum(m)==ww and i not in (0,half-1):
                continue
        out.append([8 if m[j] else 0 for j in range(ww)])
    return out