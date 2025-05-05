import sys
def solve(grid):
    H=len(grid); W=len(grid[0])
    frame=grid[0][0]
    vis=[[False]*W for _ in range(H)]
    comps=[]
    for i in range(H):
        for j in range(W):
            if grid[i][j]!=frame and not vis[i][j]:
                c=grid[i][j]
                stack=[(i,j)]; vis[i][j]=True; coords=[]
                while stack:
                    x,y=stack.pop(); coords.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny]=True; stack.append((nx,ny))
                rs=[r for r,_ in coords]; cs=[cc for _,cc in coords]
                h=max(rs)-min(rs)+1; w=max(cs)-min(cs)+1
                comps.append((h*w,h,w,c))
    comps.sort(key=lambda x:x[0])
    dims=[(h,w,c) for _,h,w,c in comps]
    Hlist=[]; mh=0
    for h,w,c in dims:
        mh=max(mh,h); Hlist.append(mh)
    Wlist=[]; mw=0
    for h,w,c in dims:
        mw=max(mw,w); Wlist.append(mw)
    outH=Hlist[-1]; outW=Wlist[-1]
    out=[[dims[-1][2]]*outW for _ in range(outH)]
    for r in range(outH):
        for cc in range(outW):
            ir=0
            while ir<len(Hlist) and r>=Hlist[ir]: ir+=1
            ic=0
            while ic<len(Wlist) and cc>=Wlist[ic]: ic+=1
            k=ir if ir>ic else ic
            out[r][cc]=dims[k][2]
    return out

if __name__=="__main__":
    data=sys.stdin.read().strip().split()
    H=int(data[0]); W=int(data[1])
    vals=list(map(int,data[2:]))
    grid=[vals[i*W:(i+1)*W] for i in range(H)]
    res=solve(grid)
    for row in res:
        print(' '.join(map(str,row)))