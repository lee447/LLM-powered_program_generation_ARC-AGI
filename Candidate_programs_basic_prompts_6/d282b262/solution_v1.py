def solve(grid):
    h=len(grid); w=len(grid[0])
    seen=[[False]*w for _ in range(h)]
    clusters=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not seen[i][j]:
                color=grid[i][j]
                comp=[(i,j)]
                seen[i][j]=True
                q=[(i,j)]
                while q:
                    x,y=q.pop()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]!=0:
                            seen[nx][ny]=True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                rs=[p[0] for p in comp]; cs=[p[1] for p in comp]
                r0,r1=min(rs),max(rs); c0,c1=min(cs),max(cs)
                shape=[row[c0:c1+1] for row in grid[r0:r1+1]]
                clusters.append({'r0':r0,'c0':c0,'r1':r1,'c1':c1,'shape':shape,'h':r1-r0+1,'w':c1-c0+1})
    # group into bands by overlapping/touching rows
    bands=[]
    used=[False]*len(clusters)
    for i,ci in enumerate(clusters):
        if used[i]: continue
        band=[i]
        used[i]=True
        changed=True
        while changed:
            changed=False
            for j,cj in enumerate(clusters):
                if used[j]: continue
                for k in band:
                    a=clusters[k]; b=clusters[j]
                    if not (a['r1']<b['r0']-1 or b['r1']<a['r0']-1):
                        band.append(j); used[j]=True; changed=True; break
        bands.append(band)
    # sort bands by min row0
    bands.sort(key=lambda b: min(clusters[i]['r0'] for i in b))
    # compute max slot width
    Wmax=max(c['w'] for c in clusters)
    c_left=w-2*Wmax; c_right=w-Wmax
    out=[[0]*w for _ in range(h)]
    single_count=0
    for band in bands:
        mb=len(band)
        if mb>=2:
            band_sorted=sorted(band, key=lambda i: clusters[i]['c0'])
            for idx,i in enumerate(band_sorted[:2]):
                slot=c_left if idx==0 else c_right
                c0=slot + -(- (Wmax-clusters[i]['w'])//2)
                for dr in range(clusters[i]['h']):
                    for dc in range(clusters[i]['w']):
                        out[clusters[i]['r0']+dr][c0+dc]=clusters[i]['shape'][dr][dc]
        else:
            single_count+=1
            i=band[0]
            slot = c_right if single_count%2==1 else c_left
            c0=slot + -(- (Wmax-clusters[i]['w'])//2)
            for dr in range(clusters[i]['h']):
                for dc in range(clusters[i]['w']):
                    out[clusters[i]['r0']+dr][c0+dc]=clusters[i]['shape'][dr][dc]
    return out