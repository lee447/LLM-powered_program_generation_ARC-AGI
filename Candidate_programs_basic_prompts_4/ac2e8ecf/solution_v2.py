def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c != 0 and not visited[i][j]:
                pts = [(i,j)]
                visited[i][j] = True
                q = [(i,j)]
                for y,x in q:
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == c:
                            visited[ny][nx] = True
                            q.append((ny,nx))
                            pts.append((ny,nx))
                miny = min(p[0] for p in pts)
                maxy = max(p[0] for p in pts)
                minx = min(p[1] for p in pts)
                maxx = max(p[1] for p in pts)
                ph = maxy - miny + 1
                pw = maxx - minx + 1
                pattern = [[0]*pw for _ in range(ph)]
                for y,x in pts:
                    pattern[y-miny][x-minx] = grid[y][x]
                shapes.append((miny, minx, ph, pw, pattern))
    shapes.sort(key=lambda s:(s[0],s[1]))
    lines = []
    line = []
    lw = 0
    lh = 0
    for s in shapes:
        _,_,ph,pw,_ = s
        if line and lw + pw > w:
            lines.append((line, lh))
            line = []
            lw = 0
            lh = 0
        line.append(s)
        lw += pw
        lh = max(lh, ph)
    if line:
        lines.append((line, lh))
    out = [[0]*w for _ in range(h)]
    yoff = 0
    for line, lh in lines:
        xoff = 0
        for _,_,ph,pw,pat in line:
            for yy in range(ph):
                for xx in range(pw):
                    if pat[yy][xx] != 0 and 0 <= yoff+yy < h and 0 <= xoff+xx < w:
                        out[yoff+yy][xoff+xx] = pat[yy][xx]
            xoff += pw
        yoff += lh
    return out