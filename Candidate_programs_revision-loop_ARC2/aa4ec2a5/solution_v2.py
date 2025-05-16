def solve(grid):
    h=len(grid);w=len(grid[0])
    vis=[[False]*w for _ in range(h)]
    comps=[]
    for y in range(h):
        for x in range(w):
            if grid[y][x]==1 and not vis[y][x]:
                stack=[(y,x)];vis[y][x]=True
                miny=maxy=y;minx=maxx=x
                while stack:
                    cy,cx=stack.pop()
                    miny,minx=min(miny,cy),min(minx,cx)
                    maxy,maxx=max(maxy,cy),max(maxx,cx)
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy+dy, cx+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx]==1:
                            vis[ny][nx]=True
                            stack.append((ny,nx))
                cy=(miny+maxy+1)//2;cx=(minx+maxx+1)//2
                comps.append((cy,cx))
    pattern=[[2 if i in (0,6) or j in (0,6) else 8 if i in (1,5) or j in (1,5) else 6 for j in range(7)] for i in range(7)]
    out=[row[:] for row in grid]
    for cy,cx in comps:
        for dy in range(-3,4):
            for dx in range(-3,4):
                y=cy+dy; x=cx+dx
                if 0<=y<h and 0<=x<w:
                    out[y][x]=pattern[dy+3][dx+3]
    return out