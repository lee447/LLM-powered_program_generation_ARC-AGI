import collections
def solve(grid):
    H=len(grid)
    W=len(grid[0])
    visited=[[False]*W for _ in range(H)]
    comps=[]
    for r in range(H):
        for c in range(W):
            v=grid[r][c]
            if v!=0 and not visited[r][c]:
                stack=[(r,c)]
                visited[r][c]=True
                coords=[]
                while stack:
                    x,y=stack.pop()
                    coords.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not visited[nx][ny] and grid[nx][ny]==v:
                            visited[nx][ny]=True
                            stack.append((nx,ny))
                comps.append((v,coords))
    bycolor=collections.defaultdict(list)
    for v,coords in comps:
        bycolor[v].append(coords)
    color_minc={}
    for c,cls in bycolor.items():
        m=W
        for comp in cls:
            for _,cc in comp:
                if cc<m:
                    m=cc
        color_minc[c]=m
    colors=sorted(bycolor.keys(),key=lambda c:color_minc[c])
    left,right=colors[0],colors[1]
    stats={}
    for c in (left,right):
        info=[]
        for comp in bycolor[c]:
            rs=[r for r,_ in comp]
            cs=[cc for _,cc in comp]
            r0=min(rs)
            h=max(rs)-min(rs)+1
            w=max(cs)-min(cs)+1
            a=len(comp)
            m=min(cs)
            info.append((comp,r0,h,w,a,m))
        info.sort(key=lambda x:(x[2],x[3],x[4]))
        small,large=info[0],info[1]
        stats[c]={'small':small,'large':large,'blockw':max(small[3],large[3])}
    leftw=stats[left]['blockw']
    result=[[0]*W for _ in range(H)]
    for c,start in ((left,0),(right,leftw+1)):
        compS,r0S,hS,wS,aS,mS=stats[c]['small']
        compL,r0L,hL,wL,aL,mL=stats[c]['large']
        newL0=H-hL
        newS0=newL0-hS-1
        offS_r=newS0-r0S
        offL_r=newL0-r0L
        offS_c=start-mS
        offL_c=start-mL
        for r,cc in compS:
            result[r+offS_r][cc+offS_c]=c
        for r,cc in compL:
            result[r+offL_r][cc+offL_c]=c
    return result