def solve(grid):
    H=len(grid);W=len(grid[0])
    g=[row[:] for row in grid]
    vis=[[False]*W for _ in range(H)]
    clusters=[]
    for i in range(H):
        for j in range(W):
            if grid[i][j]==5 and not vis[i][j]:
                stack=[(i,j)];comp=[]
                vis[i][j]=True
                while stack:
                    x,y=stack.pop()
                    comp.append((x,y))
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not vis[nx][ny] and grid[nx][ny]==5:
                            vis[nx][ny]=True
                            stack.append((nx,ny))
                clusters.append(comp)
    for comp in clusters:
        rows=[p[0] for p in comp];cols=[p[1] for p in comp]
        rmin,rmax,minc,maxc=min(rows),max(rows),min(cols),max(cols)
        if rmin==rmax:
            orientation='h';r=rmin;c1,c2=minc,maxc
        else:
            orientation='v';c=minc;r1,r2=rmin,rmax
        seeds=[]
        if orientation=='h':
            for j in range(c1,c2+1):
                for d in(-1,1):
                    i0=r+d
                    if 0<=i0<H and grid[i0][j]!=0 and grid[i0][j]!=5:
                        seq=[];i=i0
                        while 0<=i<H and grid[i][j]!=0 and grid[i][j]!=5:
                            seq.append(grid[i][j]);i+=d
                        if d==-1:
                            seq=seq[::-1]
                            rs=r-len(seq);re=r-1
                        else:
                            rs=r+1;re=r+len(seq)
                        seeds.append((j,seq,rs,re))
                        break
            if seeds:
                seeds.sort(key=lambda x:x[0])
                rs=min(s[2] for s in seeds);re=max(s[3] for s in seeds)
                m=len(seeds);width=c2-c1+1
                for jj in range(c1,c2+1):
                    idx=(jj-c1)%m
                    seq=seeds[idx][1]
                    for k,v in enumerate(seq):
                        g[rs+k][jj]=v
        else:
            for i in range(r1,r2+1):
                for d in(-1,1):
                    j0=c+d
                    if 0<=j0<W and grid[i][j0]!=0 and grid[i][j0]!=5:
                        seq=[];j=j0
                        while 0<=j<W and grid[i][j]!=0 and grid[i][j]!=5:
                            seq.append(grid[i][j]);j+=d
                        if d==-1:
                            seq=seq[::-1]
                            cs=c-len(seq);ce=c-1
                        else:
                            cs=c+1;ce=c+len(seq)
                        seeds.append((i,seq,cs,ce))
                        break
            if seeds:
                seeds.sort(key=lambda x:x[0])
                cs=min(s[2] for s in seeds);ce=max(s[3] for s in seeds)
                m=len(seeds);height=r2-r1+1
                for ii in range(r1,r2+1):
                    idx=(ii-r1)%m
                    seq=seeds[idx][1]
                    for k,v in enumerate(seq):
                        g[ii][cs+k]=v
    return g