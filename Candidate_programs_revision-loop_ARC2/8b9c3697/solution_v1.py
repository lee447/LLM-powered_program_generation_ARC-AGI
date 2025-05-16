def solve(grid):
    h=len(grid);w=len(grid[0])
    from collections import Counter, deque
    cnt=Counter(c for row in grid for c in row)
    bg,sec=max(cnt, key=lambda x: cnt[x]),2
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    def comps(color):
        seen=[[False]*w for _ in range(h)]
        cl=[]
        for i in range(h):
            for j in range(w):
                if not seen[i][j] and grid[i][j]==color:
                    q=deque([(i,j)]);seen[i][j]=True;comp=[]
                    while q:
                        x,y=q.popleft();comp.append((x,y))
                        for dx,dy in dirs:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==color:
                                seen[nx][ny]=True;q.append((nx,ny))
                    cl.append(comp)
        return cl
    prims=[]
    for color in set(cnt):
        if color!=bg and color!=sec:
            for c in comps(color):
                prims.append((len(c),color,c))
    if not prims: return grid
    prims.sort(reverse=True)
    maxsz=prims[0][0]
    prims=[c for c in prims if c[0]*2>=maxsz]
    seccl=comps(sec)
    used=set()
    for _,color,pc in prims:
        best=None
        for sc in seccl:
            if tuple(sc) in used: continue
            for (r1,c1) in sc:
                for (r2,c2) in pc:
                    if r1==r2 or c1==c2:
                        d=abs(r1-r2)+abs(c1-c2)
                        if best is None or d<best[0]:
                            best=(d,(r1,c1),(r2,c2),sc)
        if not best: continue
        _,p, q, sc=best
        used.add(tuple(sc))
        r1,c1=p; r2,c2=q
        if r1==r2:
            d=1 if c1>c2 else -1
            grid[r1][c2+d]=sec
            for y in range(c2+2*d,c1+ d,d):
                grid[r1][y]=0
        else:
            d=1 if r1>r2 else -1
            grid[r2+d][c1]=sec
            for x in range(r2+2*d,r1+ d,d):
                grid[x][c1]=0
        # erase original
        for (x,y) in sc:
            grid[x][y]=bg
    return grid