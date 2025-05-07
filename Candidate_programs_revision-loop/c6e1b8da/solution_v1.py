def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not seen[i][j]:
                c = grid[i][j]
                stack = [(i,j)]
                seen[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not seen[nx][ny] and grid[nx][ny]==c:
                            seen[nx][ny] = True
                            stack.append((nx,ny))
                rs = [r for r,_ in cells]
                cs = [c0 for _,c0 in cells]
                r0,r1 = min(rs), max(rs)
                c0,c1 = min(cs), max(cs)
                shape = set((r-r0, c-c0) for r,c in cells)
                comps.append((r0, c0, r1-r0+1, c1-c0+1, grid[r0][c0], shape))
    comps.sort(key=lambda x:(x[0],x[1]))
    out = [[0]*W for _ in range(H)]
    rows = []
    for r0,c0,h,w,col,shape in comps:
        placed = False
        for row in rows:
            ok = True
            for _,_,hh,_,_,_ in row:
                if not (r0+hh<=row[0][0] or row[0][0]+row[0][2]<=r0):
                    ok = False
                    break
            if ok:
                row.append((r0,c0,h,w,col,shape))
                placed = True
                break
        if not placed:
            rows.append([(r0,c0,h,w,col,shape)])
    y = 0
    for row in rows:
        x = 0
        maxh = 0
        for _,_,h,w,col,shape in row:
            for dy,dx in shape:
                out[y+dy][x+dx] = col
            x += w
            maxh = max(maxh, h)
        y += maxh
    return out