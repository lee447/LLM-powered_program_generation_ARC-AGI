def solve(grid):
    h=len(grid); w=len(grid[0])
    c=None
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0:
                c=grid[i][j]; break
        if c is not None: break
    vis=[[False]*w for _ in range(h)]
    comps=[]
    from collections import deque
    for i in range(h):
        for j in range(w):
            if grid[i][j]==c and not vis[i][j]:
                q=deque([(i,j)]); vis[i][j]=True
                pts=[]
                while q:
                    x,y=q.popleft()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny]=True
                            q.append((nx,ny))
                xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
                minx,maxx,miny,maxy=min(xs),max(xs),min(ys),max(ys)
                comps.append((pts,minx,maxx,miny,maxy))
    # pick comp with minimal area of bounding box among those with height==width if any, else minimal area
    best=None
    best_area=None
    for pts,minx,maxx,miny,maxy in comps:
        h0=maxx-minx+1; w0=maxy-miny+1; area=h0*w0
        if best is None:
            best=(pts,minx,maxx,miny,maxy); best_area=area; best_sq=(h0==w0)
        else:
            sq=(h0==w0)
            if best_sq and not sq:
                continue
            if sq and not best_sq:
                best=(pts,minx,maxx,miny,maxy); best_area=area; best_sq=sq
            else:
                if area<best_area:
                    best=(pts,minx,maxx,miny,maxy); best_area=area; best_sq=sq
    pts,minx,maxx,miny,maxy=best
    H=maxx-minx+1; W=maxy-miny+1
    out=[[0]*W for _ in range(H)]
    for x,y in pts:
        out[x-minx][y-miny]=c
    return out