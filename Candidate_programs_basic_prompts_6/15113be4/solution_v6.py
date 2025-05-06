def solve(grid):
    h=len(grid); w=len(grid[0])
    sep_rows=[i for i in range(h) if all(c==4 for c in grid[i])]
    sep_cols=[j for j in range(w) if all(grid[i][j]==4 for i in range(h))]
    row_segs=[]
    prev=0
    for r in sep_rows:
        row_segs.append((prev,r))
        prev=r+1
    if prev<h: row_segs.append((prev,h))
    col_segs=[]
    prev=0
    for c in sep_cols:
        col_segs.append((prev,c))
        prev=c+1
    if prev<w: col_segs.append((prev,w))
    hc=None
    for i in range(h):
        for j in range(w):
            if grid[i][j] not in (0,1,4):
                hc=grid[i][j]; break
        if hc!=None: break
    from collections import deque
    def find_ref():
        vis=[[False]*w for _ in range(h)]
        best=[]
        for rs,re in row_segs:
            for cs,ce in col_segs:
                pts=[(i,j) for i in range(rs,re) for j in range(cs,ce) if grid[i][j]==hc]
                for p in pts:
                    if not vis[p[0]][p[1]]:
                        q=deque([p]); comp=[]; vis[p[0]][p[1]]=True
                        while q:
                            x,y=q.popleft(); comp.append((x,y))
                            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                                nx,ny=x+dx,y+dy
                                if rs<=nx<re and cs<=ny<ce and not vis[nx][ny] and grid[nx][ny]==hc:
                                    vis[nx][ny]=True; q.append((nx,ny))
                        if len(comp)>len(best): best=comp
        return best
    ref=find_ref()
    if not ref: return grid
    cx=sum(x for x,y in ref)/len(ref)
    cy=sum(y for x,y in ref)/len(ref)
    pts=[(x-cx,y-cy) for x,y in ref]
    for rs,re in row_segs:
        for cs,ce in col_segs:
            one_pts=[(i,j) for i in range(rs,re) for j in range(cs,ce) if grid[i][j]==1]
            if not one_pts: continue
            # find single comp of 1
            vis=[[False]*w for _ in range(h)]
            comps=[]
            for p in one_pts:
                if not vis[p[0]][p[1]]:
                    q=deque([p]); comp=[]; vis[p[0]][p[1]]=True
                    while q:
                        x,y=q.popleft(); comp.append((x,y))
                        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                            nx,ny=x+dx,y+dy
                            if rs<=nx<re and cs<=ny<ce and not vis[nx][ny] and grid[nx][ny]==1:
                                vis[nx][ny]=True; q.append((nx,ny))
                    comps.append(comp)
            comp=max(comps,key=len) if comps else []
            if not comp: continue
            tcx=sum(x for x,y in comp)/len(comp)
            tcy=sum(y for x,y in comp)/len(comp)
            dx=tcx-cx; dy=tcy-cy
            for ox,oy in pts:
                ti=int(round(ox+cx+dx)); tj=int(round(oy+cy+dy))
                if 0<=ti<h and 0<=tj<w and grid[ti][tj]==1:
                    grid[ti][tj]=hc
    return grid