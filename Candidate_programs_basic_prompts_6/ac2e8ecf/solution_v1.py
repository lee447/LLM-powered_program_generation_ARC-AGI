def solve(grid):
    from collections import deque
    h, w = len(grid), len(grid[0])
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not seen[i][j]:
                c = grid[i][j]
                q = deque([(i,j)])
                pts = []
                seen[i][j] = True
                while q:
                    y,x = q.popleft()
                    pts.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0 <= ny < h and 0 <= nx < w and not seen[ny][nx] and grid[ny][nx]==c:
                            seen[ny][nx] = True
                            q.append((ny,nx))
                miny = min(y for y,x in pts)
                maxy = max(y for y,x in pts)
                minx = min(x for y,x in pts)
                maxx = max(x for y,x in pts)
                shape = [(y-miny, x-minx) for y,x in pts]
                comps.append((miny, minx, maxy-miny+1, maxx-minx+1, c, shape))
    comps.sort(key=lambda x:(x[0], x[1]))
    n = len(comps)
    import math
    row_size = int(math.ceil(math.sqrt(n)))
    rows = []
    for i in range(0, n, row_size):
        rows.append(comps[i:i+row_size])
    # compute output size
    out = [[0]*w for _ in range(h)]
    y_off = 0
    for row in rows:
        row_h = max(r[2] for r in row)
        x_off = 0
        for _,_,sh,sw,c,shp in row:
            for dy,dx in shp:
                out[y_off+dy][x_off+dx] = c
            x_off += sw + 1
        y_off += row_h + 1
    return out