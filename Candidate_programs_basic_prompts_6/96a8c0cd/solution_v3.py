def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    # find seed
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 2:
                sy, sx = i, j
    # find clusters (cells !=0,!=2), flood to get each cluster
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] not in (0,2) and not seen[i][j]:
                col = grid[i][j]
                q = [(i,j)]
                seen[i][j] = True
                cells = [(i,j)]
                for y,x in q:
                    for dy,dx in dirs:
                        ny, nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and not seen[ny][nx] and grid[ny][nx]==col:
                            seen[ny][nx] = True
                            q.append((ny,nx))
                            cells.append((ny,nx))
                ys = [y for y,x in cells]
                xs = [x for y,x in cells]
                y1,y2 = min(ys), max(ys)
                x1,x2 = min(xs), max(xs)
                cy = (y1+y2)//2
                cx = (x1+x2)//2
                # pick target above if possible else left
                if y1>0 and grid[y1-1][cx]==0:
                    ty, tx, L = y1-1, cx, x2-x1+1
                elif x1>0 and grid[cy][x1-1]==0:
                    ty, tx, L = cy, x1-1, y2-y1+1
                elif x2<w-1 and grid[cy][x2+1]==0:
                    ty, tx, L = cy, x2+1, y2-y1+1
                else:
                    ty, tx, L = y2+1, cx, x2-x1+1
                clusters.append((y1, (ty,tx,L)))
    clusters.sort()
    out = [row[:] for row in grid]
    cy, cx = sy, sx
    for _, (ty,tx,L) in clusters:
        # draw connecting L-shape: vertical then horizontal
        dy = 1 if ty>cy else -1
        while cy!=ty:
            cy+=dy
            if out[cy][cx]==0: out[cy][cx]=2
        dx = 1 if tx>cx else -1
        while cx!=tx:
            cx+=dx
            if out[cy][cx]==0: out[cy][cx]=2
        # draw segment of length L starting at (ty,tx) to the right
        for d in range(L):
            x = tx + d
            if 0<=x<w and out[ty][x]==0: out[ty][x]=2
        # set current to end of that segment
        cx = tx+L-1; cy = ty
    return out