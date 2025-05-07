def solve(grid):
    R, C = len(grid), len(grid[0])
    col = next(c for row in grid for c in row if c!=0)
    seen = [[False]*C for _ in range(R)]
    comps=[]
    for i in range(R):
        for j in range(C):
            if grid[i][j]==col and not seen[i][j]:
                q=[(i,j)]; seen[i][j]=True; pts=[]
                for x,y in q:
                    pts.append((x,y))
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<R and 0<=ny<C and grid[nx][ny]==col and not seen[nx][ny]:
                            seen[nx][ny]=True; q.append((nx,ny))
                rs=[p[0] for p in pts]; cs=[p[1] for p in pts]
                r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
                sub=[row[minc:maxc+1] for row in grid[r0:r1+1]]
                comps.append((r1-r0+1,maxc-minc+1,sub))
    h0,w0,sub0=comps[0]
    h1,w1,sub1=comps[1]
    if abs(h0-w0)<=abs(h1-w1):
        h,w,sub=h0,w0,sub0
    else:
        h,w,sub=h1,w1,sub1
    th = h//2 if h%2==0 else h-1
    tw = w//2 if w%2==0 else w-1
    r_off = (h-th)//2
    c_off = (w-tw)//2
    out=[row[c_off:c_off+tw] for row in sub[r_off:r_off+th]]
    return out