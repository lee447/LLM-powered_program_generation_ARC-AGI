import collections,collections,math,sys
def solve(grid):
    h,len0=len(grid),len(grid[0])
    cnt=collections.Counter(c for row in grid for c in row)
    frame_color=cnt.most_common(1)[0][0]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    h0,w0=h,len0
    seen=[[False]*w0 for _ in range(h0)]
    from collections import deque
    dq=deque()
    outside=[[False]*w0 for _ in range(h0)]
    for i in range(h0):
        for j in range(w0):
            if (i==0 or j==0 or i==h0-1 or j==w0-1) and grid[i][j]!=frame_color and not seen[i][j]:
                seen[i][j]=True
                dq.append((i,j))
                outside[i][j]=True
    while dq:
        x,y=dq.popleft()
        for dx,dy in dirs:
            nx,ny=x+dx,y+dy
            if 0<=nx<h0 and 0<=ny<w0 and not seen[nx][ny] and grid[nx][ny]!=frame_color:
                seen[nx][ny]=True
                outside[nx][ny]=True
                dq.append((nx,ny))
    interior_mask=[[False]*w0 for _ in range(h0)]
    for i in range(h0):
        for j in range(w0):
            if grid[i][j]!=frame_color and not outside[i][j]:
                interior_mask[i][j]=True
    bg=0
    comps=[]
    seen2=[[False]*w0 for _ in range(h0)]
    for i in range(h0):
        for j in range(w0):
            if interior_mask[i][j] and grid[i][j]!=bg and not seen2[i][j]:
                c0=grid[i][j]
                dq=deque([(i,j)])
                seen2[i][j]=True
                comp=[]
                while dq:
                    x,y=dq.popleft()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h0 and 0<=ny<w0 and interior_mask[nx][ny] and not seen2[nx][ny] and grid[nx][ny]==c0:
                            seen2[nx][ny]=True
                            dq.append((nx,ny))
                comps.append(comp)
    uniq=[]
    sigset=set()
    for comp in comps:
        cells=sorted(comp)
        rr=min(x for x,y in cells); cc=min(y for x,y in cells)
        offs=tuple((x-rr,y-cc) for x,y in cells)
        clrs=tuple(grid[x][y] for x,y in cells)
        sig=(offs,clrs)
        if sig not in sigset:
            sigset.add(sig)
            uniq.append((offs,clrs))
    shapes=sorted(uniq,key=lambda oc:oc[1])
    S=int(math.sqrt(len(shapes[0][0])))
    mins=min(i for i in range(h0) for j in range(w0) if interior_mask[i][j])
    minr=min(i for i in range(h0) for j in range(w0) if interior_mask[i][j])
    maxr=max(i for i in range(h0) for j in range(w0) if interior_mask[i][j])
    minc=min(j for i in range(h0) for j in range(w0) if interior_mask[i][j])
    maxc=max(j for i in range(h0) for j in range(w0) if interior_mask[i][j])
    places=[]
    for i in range(minr,maxr-S+1, S):
        for j in range(minc,maxc-S+1, S):
            ok=True
            for dr,dc in shapes[0][0]:
                if not interior_mask[i+dr][j+dc]:
                    ok=False; break
            if ok:
                places.append((i,j))
    out=[row[:] for row in grid]
    for i in range(h0):
        for j in range(w0):
            if interior_mask[i][j]:
                out[i][j]=bg
    for idx,(r,c) in enumerate(sorted(places)):
        offs,clrs=shapes[idx%len(shapes)]
        for (dr,dc),clr in zip(offs,clrs):
            out[r+dr][c+dc]=clr
    return out