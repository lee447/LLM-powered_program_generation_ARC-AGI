def solve(grid):
    h=len(grid); w=len(grid[0])
    bg=max({c:sum(row.count(c) for row in grid) for c in set(sum(grid,[]))}, key=lambda x:{c:sum(row.count(c) for row in grid) for c in set(sum(grid,[]))}[x])
    vis=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if not vis[i][j] and grid[i][j]!=bg:
                col=grid[i][j]
                stack=[(i,j)]; pts=[]; vis[i][j]=True
                while stack:
                    y,x=stack.pop()
                    pts.append((y,x))
                    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and not vis[ny][nx] and grid[ny][nx]==col:
                            vis[ny][nx]=True
                            stack.append((ny,nx))
                ys=[p[0] for p in pts]; xs=[p[1] for p in pts]
                comps.append((col, pts, min(ys), min(xs), max(ys)-min(ys)+1, max(xs)-min(xs)+1))
    block_comps=[c for c in comps if c[5]>1 or c[4]>1]
    one_comps=[c for c in comps if c[5]==1 and c[4]==1]
    block_comps.sort(key=lambda c:c[3])
    cnt={}
    for col,pts,_,x,_,_ in one_comps:
        cnt[x]=cnt.get(x,0)+1
    dc=sorted(cnt.items(), key=lambda kv:(-kv[1],kv[0]))
    drive_cols=[x for x,_ in dc[:len(block_comps)]]
    drive_cols.sort()
    block_comps.sort(key=lambda c:c[3])
    drive_rows={c:sorted(p[0] for col,pts,_,x,_,_ in one_comps if x==c for p in [(None,None)] ) for c in drive_cols}
    # better rebuild drive_rows
    drive_rows={}
    for dcol in drive_cols:
        rows=[]
        for col,pts,_,x,_,_ in one_comps:
            if x==dcol:
                rows.append(pts[0][0])
        rows=sorted(rows)
        drive_rows[dcol]=rows
    # assume all drive_cols share same drive_rows list
    drs=drive_rows[drive_cols[0]]
    if len(drs)>1:
        drive_spacing=drs[1]-drs[0]
    else:
        drive_spacing=0
    out=[row[:] for row in grid]
    for bidx,(colc,pts,minr,minc,hc,wc) in enumerate(block_comps):
        dc_col=drive_cols[bidx]
        sign=1 if minr*2<h else -1
        period=hc+drive_spacing
        for k,row_dr in enumerate(drs):
            nr=minr+sign*(period*k)
            if k==0: continue
            if 0<=nr and nr+hc<=h:
                color=grid[drs[k]][dc_col]
                for y,x in pts:
                    dy=y-minr; dx=x-minc
                    out[nr+dy][minc+dx]=color
    return out