def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 1 and not visited[i][j]:
                color = grid[i][j]
                pts = []
                stack = [(i,j)]
                visited[i][j] = True
                while stack:
                    x,y = stack.pop()
                    pts.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==color:
                            visited[nx][ny] = True
                            stack.append((nx,ny))
                xs = [p[0] for p in pts]
                ys = [p[1] for p in pts]
                minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
                cx, cy = (minx+maxx)/2, (miny+maxy)/2
                newpts = set(pts)
                transforms = [
                    lambda dx,dy:( dx, dy),
                    lambda dx,dy:(-dy, dx),
                    lambda dx,dy:(-dx,-dy),
                    lambda dx,dy:( dy,-dx),
                    lambda dx,dy:(-dx, dy),
                    lambda dx,dy:( dx,-dy),
                    lambda dx,dy:( dy, dx),
                    lambda dx,dy:(-dy,-dx),
                ]
                for x,y in pts:
                    dx, dy = x-cx, y-cy
                    for T in transforms:
                        dxp, dyp = T(dx,dy)
                        xp, yp = cx+dxp, cy+dyp
                        if abs(xp-round(xp))<1e-6 and abs(yp-round(yp))<1e-6:
                            newpts.add((int(round(xp)), int(round(yp))))
                if len(pts) <= 2:
                    if abs(cx-round(cx))<1e-6 and abs(cy-round(cy))<1e-6:
                        newpts.add((int(round(cx)), int(round(cy))))
                for x,y in newpts:
                    if 0<=x<h and 0<=y<w and grid[x][y]==1:
                        res[x][y] = color
    return res