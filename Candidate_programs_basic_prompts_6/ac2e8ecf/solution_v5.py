def solve(grid):
    h=len(grid);w=len(grid[0])
    vis=[[False]*w for _ in range(h)]
    comps=[]
    for y in range(h):
        for x in range(w):
            if grid[y][x]!=0 and not vis[y][x]:
                c=grid[y][x]
                stack=[(y,x)]
                pts=[]
                vis[y][x]=True
                while stack:
                    yy,xx=stack.pop()
                    pts.append((yy,xx))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = yy+dy, xx+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx]==c:
                            vis[ny][nx]=True
                            stack.append((ny,nx))
                ys=[p[0] for p in pts]; xs=[p[1] for p in pts]
                y0,y1,minx,maxx=min(ys),max(ys),min(xs),max(xs)
                is_border = all(grid[y0][x]==c for x in range(minx,maxx+1)) and all(grid[y1][x]==c for x in range(minx,maxx+1))
                comps.append({'pts':pts,'c':c,'y0':y0,'y1':y1,'x0':minx,'x1':maxx,'border':is_border})
    border=[c for c in comps if c['border']]
    cross=[c for c in comps if not c['border']]
    border.sort(key=lambda c:c['y0'])
    cross.sort(key=lambda c:c['y0'])
    out=[[0]*w for _ in range(h)]
    placed=[]
    for comp in border:
        dy = -comp['y0']
        while True:
            conflict=False
            for yy,xx in comp['pts']:
                ty=yy+dy; tx=xx
                if out[ty][tx]!=0:
                    conflict=True; break
            if not conflict: break
            dy+=1
        for yy,xx in comp['pts']:
            out[yy+dy][xx]=comp['c']
    for comp in cross:
        dy = (h-1)-comp['y1']
        while True:
            conflict=False
            for yy,xx in comp['pts']:
                ty=yy+dy; tx=xx
                if out[ty][tx]!=0:
                    conflict=True; break
            if not conflict: break
            dy-=1
        for yy,xx in comp['pts']:
            out[yy+dy][xx]=comp['c']
    return out