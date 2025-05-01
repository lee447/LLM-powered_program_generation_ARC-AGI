def solve(grid):
    h, w = len(grid), len(grid[0])
    sep = max({v:0 for row in grid for v in row if v!=0}, key=lambda c: max((r for r in range(h) for cc in range(w) if grid[r][cc]==c), default=0))
    vis = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==sep and not vis[i][j]:
                q=[(i,j)]; vis[i][j]=True; rs,cs=[i],[j]
                for x,y in q:
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==sep:
                            vis[nx][ny]=True; q.append((nx,ny)); rs.append(nx); cs.append(ny)
                comps.append((min(rs),max(rs),min(cs),max(cs)))
    rows = {0,h}
    cols = {0,w}
    for r0,r1,c0,c1 in comps:
        rows.add(r0); rows.add(r1+1)
        cols.add(c0); cols.add(c1+1)
    rs = sorted(rows)
    cs = sorted(cols)
    out = []
    for a,b in zip(rs,rs[1:]):
        row = []
        for c,d in zip(cs,cs[1:]):
            if b>a and d>c:
                row.append(grid[a][c])
        if row:
            out.append(row)
    return out