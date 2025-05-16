def solve(grid):
    h = len(grid)
    w = len(grid[0])
    visited = [[False]*w for _ in range(h)]
    clusters = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c and not visited[i][j]:
                pts = [(i,j)]
                visited[i][j] = True
                q = [(i,j)]
                while q:
                    x,y = q.pop()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==c:
                            visited[nx][ny] = True
                            pts.append((nx,ny))
                            q.append((nx,ny))
                clusters.setdefault(c, []).append(pts)
    P = None
    for c, cls in clusters.items():
        for pts in cls:
            xs = [x for x,y in pts]
            ys = [y for x,y in pts]
            mi,mx,miny,maxy = min(xs),max(xs),min(ys),max(ys)
            interior = []
            for i in range(mi+1,mx):
                for j in range(miny+1,maxy):
                    v = grid[i][j]
                    if v!=0 and v!=c:
                        interior.append((i,j,v))
            if len(interior)==4:
                interior.sort()
                i0,j0,_ = interior[0]
                i1,j1,_ = interior[-1]
                P = [[0,0],[0,0]]
                for i,j,v in interior:
                    ii = 0 if i==i0 else 1
                    jj = 0 if j==j0 else 1
                    P[ii][jj] = v
                break
        if P: break
    N = max(h,w)
    N = (interior and (len(interior)*0+ ((max(h,w)//2)*0+0))) or max(h,w)
    # we want square sized according to input examples: compute d = abs(pts[0][0]-pts[-1][0])
    # fallback: for 2x2 P produce 2*2*2 size
    size = None
    if P and len(P)==2:
        size = (abs(interior[0][0]-interior[-1][0]) + abs(interior[0][1]-interior[-1][1]))*2
    if not size or size<1:
        size = h if h==w else max(h,w)
    N = size
    out = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i+j < N-1:
                if i<j:
                    v = P[0][0]
                else:
                    v = P[0][1]
            else:
                if i<j:
                    v = P[1][0]
                else:
                    v = P[1][1]
            out[i][j] = v
    return out