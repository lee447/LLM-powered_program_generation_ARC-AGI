def solve(grid):
    H,W=len(grid),len(grid[0])
    visited=[[False]*W for _ in range(H)]
    comps=[]
    for r in range(H):
        for c in range(W):
            v=grid[r][c]
            if v!=0 and not visited[r][c]:
                stack=[(r,c)]; visited[r][c]=True; coords=[]
                while stack:
                    x,y=stack.pop()
                    coords.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==v:
                            visited[nx][ny]=True
                            stack.append((nx,ny))
                comps.append((v,coords))
    bycolor={}
    for v,coords in comps:
        bycolor.setdefault(v,[]).append(coords)
    colors=list(bycolor.keys())
    color_minc={}
    for c in colors:
        m=W
        for comp in bycolor[c]:
            for _,cc in comp:
                if cc<m:m=cc
        color_minc[c]=m
    left= min(colors, key=lambda c: color_minc[c])
    right= next(c for c in colors if c!=left)
    stats={}
    for c in (left,right):
        cl=bycolor[c]
        info=[]
        for comp in cl:
            rs=[r for r,_ in comp]; cs=[c0 for _,c0 in comp]
            r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
            info.append((comp,r0,r1-min(rs)+1,maxc-minc+1,len(comp),minc))
        info.sort(key=lambda x:(x[2],x[3],x[4]))
        small,large=info[0],info[1]
        stats[c]={'small':small,'large':large,'blockw':max(small[3],large[3])}
    leftw=stats[left]['blockw']
    result=[[0]*W for _ in range(H)]
    for c,blockStart in ((left,0),(right,leftw+1)):
        st=stats[c]
        compS,r0S,hS,wS,aS,mincS=st['small']
        compL,r0L,hL,wL,aL,mincL=st['large']
        newL0=H-hL
        newS0=newL0-hS-1
        offS_r=newS0-r0S
        offL_r=newL0-r0L
        offS_c=blockStart-mincS
        offL_c=blockStart-mincL
        for r,c0 in compS:
            nr, nc = r+offS_r, c0+offS_c
            result[nr][nc]=c
        for r,c0 in compL:
            nr, nc = r+offL_r, c0+offL_c
            result[nr][nc]=c
    return result