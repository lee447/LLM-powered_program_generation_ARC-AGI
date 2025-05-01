def solve(grid):
    n,r=len(grid),len(grid[0]) if grid else 0
    visited=[[False]*r for _ in range(n)]
    comps=[]
    for i in range(n):
        for j in range(r):
            if grid[i][j]!=0 and not visited[i][j]:
                q=[(i,j)]
                visited[i][j]=True
                r0,r1,c0,c1=i,i,j,j
                idx=0
                while idx<len(q):
                    x,y=q[idx];idx+=1
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<n and 0<=ny<r and grid[nx][ny]!=0 and not visited[nx][ny]:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                            if nx<r0: r0=nx
                            if nx>r1: r1=nx
                            if ny<c0: c0=ny
                            if ny>c1: c1=ny
                comps.append((r0,r1,c0,c1))
    groups={}
    for r0,r1,c0,c1 in comps:
        h,w=r1-r0+1,c1-c0+1
        if h*w>=5:
            groups.setdefault((h,w),[]).append((r0,r1,c0,c1))
    reps={}
    for dims,blks in groups.items():
        blks.sort(key=lambda x:(x[0],x[2]))
        r0,r1,c0,c1=blks[0]
        reps[dims]=[row[c0:c1+1] for row in grid[r0:r1+1]]
    out=[[0]*r for _ in range(n)]
    for dims,blks in groups.items():
        h,w=dims
        pat=reps[dims]
        for r0,r1,c0,c1 in blks:
            for ii in range(h):
                out[r0+ii][c0:c0+w]=pat[ii][:]
    return out