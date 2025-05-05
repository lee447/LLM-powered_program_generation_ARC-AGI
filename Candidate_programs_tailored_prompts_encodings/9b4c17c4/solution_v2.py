def solve(grid):
    R, C = len(grid), len(grid[0])
    # detect boundary
    hor = ver = False
    brow = bcol = -1
    for i in range(R-1):
        if all(grid[i][j] == grid[i+1][j] for j in range(C)) and grid[i][0] != grid[i+1][0]:
            hor = True
            brow = i
            break
    if not hor:
        for j in range(C-1):
            if all(grid[i][j] == grid[i][j+1] for i in range(R)) and grid[0][j] != grid[0][j+1]:
                ver = True
                bcol = j
                break
    # flood-fill components of 2
    seen = [[False]*C for _ in range(R)]
    comps = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 2 and not seen[i][j]:
                stack = [(i,j)]
                seen[i][j] = True
                pts = []
                while stack:
                    x,y = stack.pop()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<R and 0<=ny<C and not seen[nx][ny] and grid[nx][ny]==2:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                rs = [p[0] for p in pts]
                cs = [p[1] for p in pts]
                comps.append((min(rs),max(rs),min(cs),max(cs)))
    # prepare output with region colors
    out = [[0]*C for _ in range(R)]
    if hor:
        r1color = grid[0][0]
        r2color = grid[brow+1][0]
        for i in range(R):
            for j in range(C):
                out[i][j] = r1color if i<=brow else r2color
    else:
        c1color = grid[0][0]
        c2color = grid[0][bcol+1]
        for i in range(R):
            for j in range(C):
                out[i][j] = c1color if j<=bcol else c2color
    # slide each comp
    for rmin,rmax,cmin,cmax in comps:
        h = rmax-rmin+1
        w = cmax-cmin+1
        if hor:
            if rmax <= brow:
                # region1 slide east
                ncmin = C - w
            else:
                # region2 slide west
                ncmin = 0
            for dr in range(h):
                for dc in range(w):
                    out[rmin+dr][ncmin+dc] = 2
        else:
            if cmax <= bcol:
                # region1 slide south
                nrmin = R - h
            else:
                # region2 slide north
                nrmin = 0
            for dr in range(h):
                for dc in range(w):
                    out[nrmin+dr][cmin+dc] = 2
    return out