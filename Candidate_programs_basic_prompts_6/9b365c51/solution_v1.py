def solve(grid):
    h=len(grid); w=len(grid[0])
    stripe_cols=[j for j in range(w) if any(grid[i][j]!=0 and grid[i][j]!=8 for i in range(h))]
    stripe_cols.sort()
    stripe_colors=[next(grid[i][j] for i in range(h) if grid[i][j]!=0 and grid[i][j]!=8) for j in stripe_cols]
    shape=[(i,j) for i in range(h) for j in range(w) if grid[i][j]==8]
    minr=min(i for i,j in shape); maxr=max(i for i,j in shape)
    midr=(minr+maxr)//2
    runs=[]
    j=0
    while j<w:
        if grid[midr][j]==8:
            start=j
            while j<w and grid[midr][j]==8: j+=1
            runs.append((midr,start))
        else:
            j+=1
    reps=sorted(runs,key=lambda x:x[1])
    dist_list=[]
    for rx,ry in reps:
        dist=[[None]*w for _ in range(h)]
        dist[rx][ry]=0
        q=[(rx,ry)]
        for x,y in q:
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny=x+dx,y+dy
                if 0<=nx<h and 0<=ny<w and grid[nx][ny]==8 and dist[nx][ny] is None:
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx,ny))
        dist_list.append(dist)
    out=[[0]*w for _ in range(h)]
    for i,j in shape:
        best=0
        bd=dist_list[0][i][j]
        for k in range(1,len(dist_list)):
            d=dist_list[k][i][j]
            if d<bd:
                bd=d; best=k
        out[i][j]=stripe_colors[best]
    return out