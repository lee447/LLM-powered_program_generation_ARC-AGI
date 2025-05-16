def solve(grid):
    h=len(grid);w=len(grid[0])
    from collections import deque,Counter
    cnt=Counter(x for row in grid for x in row)
    bg0=grid[0][0]
    bg1=max((c for c in cnt if c!=bg0), key=lambda c:cnt[c])
    bg={bg0,bg1}
    comp=[[-1]*w for _ in range(h)]
    region_color={}
    cid=0
    for i in range(h):
        for j in range(w):
            if comp[i][j]==-1 and grid[i][j] in bg:
                col=grid[i][j]
                dq=deque([(i,j)])
                comp[i][j]=cid
                while dq:
                    x,y=dq.popleft()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and comp[nx][ny]==-1 and grid[nx][ny]==col:
                            comp[nx][ny]=cid
                            dq.append((nx,ny))
                region_color[cid]=col
                cid+=1
    adj={i:set() for i in range(cid)}
    for i in range(h):
        for j in range(w):
            if comp[i][j]!=-1:
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni,nj=i+dx,j+dy
                    if 0<=ni<h and 0<=nj<w and comp[ni][nj]!=-1 and comp[ni][nj]!=comp[i][j]:
                        adj[comp[i][j]].add(comp[ni][nj])
    start=comp[0][0]
    order=[start]
    prev=None
    cur=start
    while True:
        nbrs=[n for n in adj[cur] if n!=prev]
        if not nbrs: break
        nxt=nbrs[0]
        order.append(nxt)
        prev,cur=cur,nxt
    shape_comp=[[-1]*w for _ in range(h)]
    shapes=[]
    sid=0
    for i in range(h):
        for j in range(w):
            if shape_comp[i][j]==-1 and grid[i][j] not in bg:
                col=grid[i][j]
                dq=deque([(i,j)])
                shape_comp[i][j]=sid
                cells=[(i,j)]
                while dq:
                    x,y=dq.popleft()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and shape_comp[nx][ny]==-1 and grid[nx][ny]==col:
                            shape_comp[nx][ny]=sid
                            dq.append((nx,ny))
                            cells.append((nx,ny))
                minr=min(x for x,y in cells);minc=min(y for x,y in cells)
                shapes.append((cells,col,minr,minc))
                sid+=1
    shape_region=[None]*sid
    for idx,(cells,col,minr,minc) in enumerate(shapes):
        for x,y in cells:
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny=x+dx,y+dy
                if 0<=nx<h and 0<=ny<w and comp[nx][ny]!=-1:
                    shape_region[idx]=comp[nx][ny]
                    break
            if shape_region[idx] is not None: break
    region_bbox={i:[h,w, h, w] for i in range(cid)}
    for i in range(h):
        for j in range(w):
            r=comp[i][j]
            if r!=-1:
                bb=region_bbox[r]
                if i<bb[0]: bb[0]=i
                if j<bb[1]: bb[1]=j
                if i>bb[2]: bb[2]=i
                if j>bb[3]: bb[3]=j
    out=[row[:] for row in grid]
    for idx,(cells,col,minr,minc) in enumerate(shapes):
        r0=shape_region[idx]
        ccol=region_color[r0]
        for x,y in cells:
            out[x][y]=ccol
    for idx,(cells,col,minr,minc) in enumerate(shapes):
        r0=shape_region[idx]
        i0=order.index(r0)
        r1=order[(i0+1)%len(order)]
        tgt_r0,tgt_c0,_2,_3=region_bbox[r1]
        for x,y in cells:
            dx,dy=x-minr,y-minc
            out[tgt_r0+dx][tgt_c0+dy]=col
    return out