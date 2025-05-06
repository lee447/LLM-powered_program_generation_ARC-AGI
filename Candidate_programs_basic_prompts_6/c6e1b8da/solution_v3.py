def solve(grid):
    h=len(grid);w=len(grid[0])
    vis=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            c=grid[i][j]
            if c!=0 and not vis[i][j]:
                pts=[(i,j)]
                vis[i][j]=True
                for k in range(len(pts)):
                    x,y=pts[k]
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny]=True
                            pts.append((nx,ny))
                rs=[p[0] for p in pts]; cs=[p[1] for p in pts]
                comps.append({'color':c,'pts':pts,'r0':min(rs),'r1':max(rs),'c0':min(cs),'c1':max(cs)})
    comps.sort(key=lambda x: x['r0'])
    dirs=['R','D','L','R']
    moves=[None]*len(comps)
    moves[0]=(0,0)
    for i in range(1,len(comps)):
        prev=comps[i-1];cur=comps[i]
        d=dirs[(i-1)%len(dirs)]
        if d=='R':
            dx=prev['c1']+1-cur['c0']; dy=prev['r0']-cur['r0']
        elif d=='L':
            dx=prev['c0']-1-cur['c1']; dy=prev['r0']-cur['r0']
        else:
            dx=prev['c0']-cur['c0']; dy=prev['r1']+1-cur['r0']
        moves[i]=(dy,dx)
    out=[[0]*w for _ in range(h)]
    for comp,move in zip(comps,moves):
        dy,dx=move
        for r,c in comp['pts']:
            nr,nc=r+dy,c+dx
            out[nr][nc]=comp['color']
    return out