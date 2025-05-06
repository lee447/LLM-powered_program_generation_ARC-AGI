def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    dirs4 = [(0,1),(1,0),(0,-1),(-1,0)]
    comps = []
    for y in range(h):
        for x in range(w):
            if grid[y][x]==3 and not visited[y][x]:
                stack = [(y,x)]
                visited[y][x] = True
                cells = []
                ymin=y; ymax=y; xmin=x; xmax=x
                while stack:
                    cy,cx = stack.pop()
                    cells.append((cy,cx))
                    ymin = min(ymin,cy); ymax = max(ymax,cy)
                    xmin = min(xmin,cx); xmax = max(xmax,cx)
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx = cy+dy,cx+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==3:
                            visited[ny][nx]=True
                            stack.append((ny,nx))
                by = ymin; bx = xmin
                bh = ymax-ymin+1; bw = xmax-xmin+1
                is_border = bh>=3 and bw>=3
                if is_border:
                    cnt = 0
                    for yy in range(by,by+bh):
                        for xx in range(bx,bx+bw):
                            if yy==by or yy==by+bh-1 or xx==bx or xx==bx+bw-1:
                                if (yy,xx) in cells: cnt +=1
                    if cnt==len(cells):
                        comps.append((by,bx,bh,bw))
    comps.sort()
    for i,(by,bx,bh,bw) in enumerate(comps):
        color = 1 if i%2==0 else 8
        d = dirs4[i%4]
        dy,dx = d
        if dx!=0:
            shift = (bw+1)*dx
            ty,tx = by, bx+shift
        else:
            shift = (bh+1)*dy
            ty,tx = by+shift, bx
        if ty<0 or tx<0 or ty+bh>h or tx+bw>w:
            d = dirs4[(i+1)%4]
            dy,dx = d
            if dx!=0:
                shift = (bw+1)*dx
                ty,tx = by, bx+shift
            else:
                shift = (bh+1)*dy
                ty,tx = by+shift, bx
        for yy in range(ty,ty+bh):
            for xx in range(tx,tx+bw):
                if yy==ty or yy==ty+bh-1 or xx==tx or xx==tx+bw-1:
                    if 0<=yy<h and 0<=xx<w and grid[yy][xx]==0:
                        grid[yy][xx] = color
    return grid