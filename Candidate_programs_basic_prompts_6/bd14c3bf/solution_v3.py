def solve(grid):
    h=len(grid);w=len(grid[0])
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    def bfs(sx,sy,color,vis):
        q=[(sx,sy)];vis.add((sx,sy));pts=[(sx,sy)]
        for x,y in q:
            for dx,dy in dirs:
                nx,ny=x+dx,y+dy
                if 0<=nx<h and 0<=ny<w and (nx,ny) not in vis and grid[nx][ny]==color:
                    vis.add((nx,ny));q.append((nx,ny));pts.append((nx,ny))
        return pts
    vis2=set()
    tpl=None
    for i in range(h):
        for j in range(w):
            if grid[i][j]==2 and (i,j) not in vis2:
                tpl=bfs(i,j,2,vis2);break
        if tpl:break
    minx=min(p[0] for p in tpl);maxx=max(p[0] for p in tpl)
    miny=min(p[1] for p in tpl);maxy=max(p[1] for p in tpl)
    th=maxx-minx+1;tw=maxy-miny+1
    vis1=set()
    out=[row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and (i,j) not in vis1:
                pts=bfs(i,j,1,vis1)
                xs=[p[0] for p in pts];ys=[p[1] for p in pts]
                mi,ma=min(xs),max(xs);mj,ma2=min(ys),max(ys)
                bh=ma-mi+1;bw=ma2-mj+1
                border=True
                for x,y in pts:
                    if not(x==mi or x==ma or y==mj or y==ma2):
                        border=False;break
                if border:
                    do=False
                    if bw>1 and bh>1:
                        if bw>=tw and bh>=th:do=True
                    elif bh==1:
                        if bw>tw:do=True
                    if do:
                        for x,y in pts:out[x][y]=2
    return out