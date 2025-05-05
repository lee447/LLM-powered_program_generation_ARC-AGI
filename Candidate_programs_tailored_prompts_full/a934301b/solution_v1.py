def solve(grid):
    h=len(grid);w=len(grid[0])
    vis=[[False]*w for _ in range(h)]
    clusters=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not vis[i][j]:
                cells=[];stk=[(i,j)];vis[i][j]=True
                while stk:
                    y,x=stk.pop()
                    cells.append((y,x))
                    for dy,dx in[(1,0),(-1,0),(0,1),(0,-1)]:
                        ny, nx = y+dy, x+dx
                        if 0<=ny<h and 0<=nx<w and grid[ny][nx]!=0 and not vis[ny][nx]:
                            vis[ny][nx]=True;stk.append((ny,nx))
                rs=[p[0] for p in cells]; cs=[p[1] for p in cells]
                minr,minc,maxr,maxc=min(rs),min(cs),max(rs),max(cs)
                cy=(minr+maxr)/2;cx=(minc+maxc)/2
                clusters.append({'cells':cells,'cy':cy,'cx':cx})
    n=len(clusters)
    pairs=[(r,n//r) for r in range(2,n+1) if n%r==0 and n//r>1]
    pairs=sorted(pairs, key=lambda rc: (rc[0]>rc[1], rc[0]))
    R,C=pairs[0]
    clusters=sorted(clusters, key=lambda c: c['cy'])
    rows=[sorted(clusters[i*C:(i+1)*C], key=lambda c: c['cx']) for i in range(R)]
    keep=[]
    if C>R:
        for i in range(R):
            keep+=rows[i][C-1]['cells'] if False else []
        kept_cells=[rows[i][C-1] for i in range(R)]
    else:
        if C==R:
            if R%2==0:
                idx=0
            else:
                idx=R//2
        else:
            idx=R-1
        kept_cells=rows[idx]
    out=[[0]*w for _ in range(h)]
    for cl in kept_cells:
        for y,x in cl['cells']:
            out[y][x]=grid[y][x]
    return out