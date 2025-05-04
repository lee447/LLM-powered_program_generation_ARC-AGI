import math

def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    trans = [(1,0,0,1),(0,-1,1,0),(-1,0,0,-1),(0,1,-1,0),(1,0,0,-1),(-1,0,0,1),(0,1,1,0),(0,-1,-1,0)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 or visited[i][j]:
                continue
            c = grid[i][j]
            stack = [(i,j)]
            visited[i][j] = True
            pts = []
            while stack:
                x,y = stack.pop()
                pts.append((x,y))
                for dx,dy in dirs:
                    nx,ny = x+dx, y+dy
                    if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == c:
                        visited[nx][ny] = True
                        stack.append((nx,ny))
            xs = [x for x,y in pts]
            ys = [y for x,y in pts]
            minx, maxx = min(xs), max(xs)
            miny, maxy = min(ys), max(ys)
            cx = (minx + maxx) / 2
            cy = (miny + maxy) / 2
            newpts = set(pts)
            for x,y in pts:
                dx, dy = x - cx, y - cy
                for a,b,c_,d in trans:
                    dxp = a*dx + b*dy
                    dyp = c_*dx + d*dy
                    xp = cx + dxp
                    yp = cy + dyp
                    if abs(xp - round(xp)) < 1e-6 and abs(yp - round(yp)) < 1e-6:
                        newpts.add((int(round(xp)), int(round(yp))))
            for x,y in newpts:
                if 0 <= x < h and 0 <= y < w and grid[x][y] == 1:
                    res[x][y] = c
    return res