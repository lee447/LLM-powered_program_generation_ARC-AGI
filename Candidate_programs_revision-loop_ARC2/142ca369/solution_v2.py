def solve(grid):
    h = len(grid)
    w = len(grid[0])
    vis = [[False]*w for _ in range(h)]
    comps = {}
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0,1), (1,-1), (1,0), (1,1)]
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c!=0 and not vis[i][j]:
                stack = [(i,j)]
                vis[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                comps.setdefault(c, []).append(cells)
    def draw_line(x0,y0,x1,y1,c):
        dx = abs(x1-x0)
        dy = abs(y1-y0)
        sx = 1 if x0<x1 else -1
        sy = 1 if y0<y1 else -1
        err = dx - dy
        while True:
            out[x0][y0] = c
            if x0==x1 and y0==y1: break
            e2 = err*2
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
    out = [row[:] for row in grid]
    for c, lst in comps.items():
        if len(lst)==2:
            a = lst[0]
            b = lst[1]
            a1 = max(a, key=lambda p: p[0]+p[1])
            b1 = min(b, key=lambda p: p[0]+p[1])
            draw_line(a1[0], a1[1], b1[0], b1[1], c)
        else:
            a = lst[0]
            rmax = max(p[0] for p in a)
            cmax = max(p[1] for p in a)
            length = max(rmax-min(p[0] for p in a), cmax-min(p[1] for p in a)) + 1
            for d in range(1, length+1):
                rr = rmax + d
                cc = cmax + d
                if 0<=rr<h and 0<=cc<w:
                    out[rr][cc] = c
    return out