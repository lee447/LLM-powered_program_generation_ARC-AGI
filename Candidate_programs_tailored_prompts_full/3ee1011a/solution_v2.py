def solve(grid):
    h=len(grid); w=len(grid[0])
    visited=[[False]*w for _ in range(h)]
    segments=[]
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=0 and not visited[r][c]:
                v=grid[r][c]
                lh=1; lc=c+1
                while lc<w and grid[r][lc]==v:
                    lh+=1; lc+=1
                lv=1; lr=r+1
                while lr<h and grid[lr][c]==v:
                    lv+=1; lr+=1
                if lh>=lv and lh>1:
                    for x in range(c,c+lh): visited[r][x]=True
                    segments.append((lh,v,r,c))
                elif lv>1:
                    for y in range(r,r+lv): visited[y][c]=True
                    segments.append((lv,v,r,c))
                else:
                    visited[r][c]=True
                    segments.append((1,v,r,c))
    segments=sorted(segments,key=lambda x:-x[0])
    n=segments[0][0]
    res=[[0]*n for _ in range(n)]
    for i,(l,v,_,_ )in enumerate(segments):
        size=n-2*i
        if size<=0: break
        t=i; lft=i; b=t+size-1; rgt=lft+size-1
        if size>2:
            for x in range(lft,rgt+1): res[t][x]=v; res[b][x]=v
            for y in range(t,b+1): res[y][lft]=v; res[y][rgt]=v
        elif size==2:
            for y in range(t,b+1):
                for x in range(lft,rgt+1):
                    res[y][x]=v
        else:
            res[t][lft]=v
    return res