def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if not vis[i][j]:
                col = grid[i][j]
                stack = [(i,j)]
                pts = []
                vis[i][j] = True
                while stack:
                    x,y = stack.pop()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==col:
                            vis[nx][ny] = True
                            stack.append((nx,ny))
                rs = [p[0] for p in pts]
                cs = [p[1] for p in pts]
                r0,r1 = min(rs), max(rs)
                c0,c1 = min(cs), max(cs)
                area = (r1-r0+1)*(c1-c0+1)
                comps.append((len(pts), area, col, r0, r1, c0, c1))
    # pick anchor: area==size and size>1, choose largest
    anchors = [c for c in comps if c[0]==c[1] and c[0]>1]
    anchors.sort(reverse=True)
    size,_,acol,r0,r1,c0,c1 = anchors[0]
    bh, bw = r1-r0+1, c1-c0+1
    # decide side
    side = None
    # vertical?
    if bh > bw:
        # stripe vertical
        # check left
        ok = any(0<=c0-1<w and grid[r][c0-1]!=acol for r in range(r0,r1+1))
        side = 'left' if ok else 'right'
        if side=='left':
            cc0,cc1 = c0-bw, c0-1
        else:
            cc0,cc1 = c1+1, c1+bw
        rr0,rr1 = r0, r1
    else:
        # horizontal or square
        ok = any(0<=r0-1<h and grid[r0-1][c]!=acol for c in range(c0,c1+1))
        side = 'up' if ok else 'down'
        if side=='up':
            rr0,rr1 = r0-bh, r0-1
        else:
            rr0,rr1 = r1+1, r1+bh
        cc0,cc1 = c0, c1
    # clip bounds
    rr0,rr1 = max(0,rr0), min(h-1,rr1)
    cc0,cc1 = max(0,cc0), min(w-1,cc1)
    out = [row[cc0:cc1+1] for row in grid[rr0:rr1+1]]
    return out