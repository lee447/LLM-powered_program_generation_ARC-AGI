def solve(grid):
    h=len(grid); w=len(grid[0])
    from collections import deque
    def comps(color):
        seen=[[False]*w for _ in range(h)]
        parts=[]
        for i in range(h):
            for j in range(w):
                if not seen[i][j] and grid[i][j]==color:
                    q=deque([(i,j)]); seen[i][j]=True; comp=[(i,j)]
                    while q:
                        x,y=q.popleft()
                        for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                            nx,ny=x+dx,y+dy
                            if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==color:
                                seen[nx][ny]=True; q.append((nx,ny)); comp.append((nx,ny))
                    parts.append(comp)
        return parts
    def is_L(comp):
        if len(comp)!=3: return False
        s=set(comp)
        for x,y in comp:
            cnt=0
            for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                if (x+dx,y+dy) in s: cnt+=1
            if cnt==2: return True
        return False
    cand=[]
    for c in set(v for row in grid for v in row if v!=0):
        p=comps(c)
        L=[comp for comp in p if is_L(comp)]
        if len(L)==2:
            pivots=[]
            for comp in L:
                s=set(comp)
                for x,y in comp:
                    cnt=0
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        if (x+dx,y+dy) in s: cnt+=1
                    if cnt==2:
                        pivots.append((x,y)); break
            (r1,c1),(r2,c2)=pivots
            area=(abs(r2-r1)+1)*(abs(c2-c1)+1)
            cand.append((area,c,pivots))
    if not cand: return grid
    area0,cc,pivots0=max(cand, key=lambda x:x[0])
    r1,c1=pivots0[0]; r2,c2=pivots0[1]
    rmin,rmax=sorted((r1,r2)); cmin,cmax=sorted((c1,c2))
    bc=max(v for row in grid for v in row)
    out=[row[:] for row in grid]
    for i in range(rmin,rmax+1):
        for j in range(cmin,cmax+1):
            if i in (rmin,rmax) or j in (cmin,cmax):
                if out[i][j]!=cc:
                    out[i][j]=bc
    return out