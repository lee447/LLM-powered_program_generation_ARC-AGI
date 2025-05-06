def solve(grid):
    n=len(grid); m=len(grid[0])
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    visited=[[False]*m for _ in range(n)]
    comps_by_color={}
    for i in range(n):
        for j in range(m):
            c=grid[i][j]
            if c>0 and not visited[i][j]:
                stack=[(i,j)]; visited[i][j]=True; comp=[(i,j)]
                while stack:
                    x,y=stack.pop()
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny]==c:
                            visited[nx][ny]=True
                            stack.append((nx,ny)); comp.append((nx,ny))
                comps_by_color.setdefault(c,[]).append(comp)
    mask_color=None
    for c,clist in comps_by_color.items():
        if len(clist)==1 and len(clist[0])>1:
            mask_color=c; break
    comp=comps_by_color[mask_color][0]
    r0=min(r for r,c in comp); r1=max(r for r,c in comp)
    c0=min(c for r,c in comp); c1=max(c for r,c in comp)
    H=r1-r0+1; W=c1-c0+1
    counts={}
    for i in range(n-H+1):
        for j in range(m-W+1):
            valid=True
            for dr in range(H):
                for dc in range(W):
                    if grid[i+dr][j+dc]==mask_color:
                        valid=False; break
                if not valid: break
            if not valid: continue
            sub=tuple(tuple(grid[i+dr][j+dc] for dc in range(W)) for dr in range(H))
            counts[sub]=counts.get(sub,0)+1
    best,bcnt=None,0
    for sub,cnt in counts.items():
        if cnt>1 and cnt>bcnt:
            best,bcnt=sub,cnt
    if best is None:
        best=max(counts.items(), key=lambda x:x[1])[0]
    return [list(row) for row in best]