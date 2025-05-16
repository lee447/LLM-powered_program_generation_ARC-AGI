import collections
def solve(grid):
    h,w=len(grid),len(grid[0])
    dirs=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    fives={(r,c) for r in range(h) for c in range(w) if grid[r][c]==5}
    adj={p:[] for p in fives}
    for r,c in fives:
        for dr,dc in dirs:
            p=(r+dr,c+dc)
            if p in fives: adj[(r,c)].append(p)
    ends=[p for p,nei in adj.items() if len(nei)==1]
    def bfs_dist(a):
        dq=collections.deque([a])
        dist={a:0}
        while dq:
            u=dq.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v]=dist[u]+1
                    dq.append(v)
        return dist
    best=(None,None,-1)
    for i in range(len(ends)):
        for j in range(i+1,len(ends)):
            a,b=ends[i],ends[j]
            d=bfs_dist(a).get(b,-1)
            if d>best[2]: best=(a,b,d)
    a,b,_=best
    def get_cluster(p):
        seed=None
        for dr,dc in dirs:
            nr,nc=p[0]+dr,p[1]+dc
            if 0<=nr<h and 0<=nc<w and grid[nr][nc] not in (0,5):
                seed=(nr,nc); break
        vis={seed}
        dq=[seed]
        while dq:
            x,y=dq.pop()
            for dr,dc in dirs:
                xx,yy=x+dr,y+dc
                if 0<=xx<h and 0<=yy<w and grid[xx][yy] not in (0,5) and (xx,yy) not in vis:
                    vis.add((xx,yy)); dq.append((xx,yy))
        return vis
    ca_cells=get_cluster(a)
    cb_cells=get_cluster(b)
    def center(cells):
        rs=[r for r,c in cells]; cs=[c for r,c in cells]
        return ((min(rs)+max(rs))//2,(min(cs)+max(cs))//2)
    ar,ac=center(ca_cells)
    br,bc=center(cb_cells)
    centerA=(ar,ac); centerB=(br,bc)
    for r,c in ca_cells:
        if (r,c)!=centerA: borderA=grid[r][c]; break
    for r,c in cb_cells:
        if (r,c)!=centerB: borderB=grid[r][c]; break
    out=[[0]*w for _ in range(h)]
    for r,c in fives: out[r][c]=5
    for r,c in ca_cells:
        out[r][c]=borderA if (r,c)!=centerA else borderB
    for r,c in cb_cells:
        out[r][c]=borderB if (r,c)!=centerB else borderA
    return out