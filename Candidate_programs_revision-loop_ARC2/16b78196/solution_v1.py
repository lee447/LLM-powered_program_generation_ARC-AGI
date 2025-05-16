def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import deque, defaultdict
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c and c!=8 and not seen[i][j]:
                q = deque([(i,j)])
                seen[i][j]=True
                pts = []
                while q:
                    x,y=q.popleft()
                    pts.append((x,y))
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==c:
                            seen[nx][ny]=True
                            q.append((nx,ny))
                xs=[p[1] for p in pts]; ys=[p[0] for p in pts]
                comps.append({'color':c,'pts':pts,'minx':min(xs),'maxx':max(xs),
                              'miny':min(ys),'maxy':max(ys)})
    # background
    seen2=[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==8 and not seen2[i][j]:
                q=deque([(i,j)]); seen2[i][j]=True; bpts=[]
                while q:
                    x,y=q.popleft(); bpts.append((x,y))
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen2[nx][ny] and grid[nx][ny]==8:
                            seen2[nx][ny]=True; q.append((nx,ny))
                bx=[p[1] for p in bpts]; by=[p[0] for p in bpts]
                bg={'minx':min(bx),'maxx':max(bx),'miny':min(by),'maxy':max(by)}
                break
    above = [c for c in comps if c['maxy']<bg['miny']]
    below = [c for c in comps if c['miny']>bg['maxy']]
    out = [row[:] for row in grid]
    # clear non-8 non-zero
    for i in range(h):
        for j in range(w):
            if out[i][j]!=8 and out[i][j]!=0:
                out[i][j]=0
    def draw(comp, oy, ox):
        for y,x in comp['pts']:
            dy,dx = y-comp['miny'], x-comp['minx']
            out[oy+dy][ox+dx] = comp['color']
    # cluster above side
    if above:
        a = max(above, key=lambda c:c['maxy'])
        nb = sorted(below, key=lambda c:c['miny'])
        m = 1 if len(nb)==1 else min(2,len(nb))
        use = [a]+nb[:m]
        minw = min(c['minx'] for c in use)
        maxh = max(c['maxy']-c['miny']+1 for c in use)
        oy = bg['miny']-maxh
        ox = minw+1
        for c in use:
            draw(c, oy, ox + (c['minx']-minw))
    # cluster below side
    if below:
        na = sorted(below, key=lambda c:c['miny'], reverse=True)
        m2 = 2 if len(na)>1 else 1
        use2 = na[:m2]
        minw2 = min(c['minx'] for c in use2)
        maxh2 = max(c['maxy']-c['miny']+1 for c in use2)
        oy2 = bg['maxy']+1
        ox2 = minw2+1
        for c in use2:
            draw(c, oy2, ox2 + (c['minx']-minw2))
    return out