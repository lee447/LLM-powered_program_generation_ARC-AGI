def solve(grid):
    h,len0=len(grid),len(grid[0])
    from collections import deque
    seen=[[False]*len0 for _ in range(h)]
    comps=[]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(len0):
            if grid[i][j]!=0 and not seen[i][j]:
                col=grid[i][j]
                q=deque([(i,j)])
                seen[i][j]=True
                cells=[]
                while q:
                    x,y=q.popleft()
                    cells.append((x,y))
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<len0 and not seen[nx][ny] and grid[nx][ny]==col:
                            seen[nx][ny]=True
                            q.append((nx,ny))
                rs=[x for x,y in cells]; cs=[y for x,y in cells]
                r0,c0=min(rs),min(cs)
                comps.append((r0,col,[(x-r0,y-c0) for x,y in cells],max(rs)-r0+1,max(cs)-c0+1))
    comps.sort(key=lambda x:x[0])
    out=[[0]*len0 for _ in range(h)]
    prev=None
    for idx,(r0,col,rel,ph,pw) in enumerate(comps):
        if idx==0:
            nr,nc=r0,comps[0][1]*0 + comps[0][0]*0 + comps[0][0]*0 + comps[0][0]*0 + r0
            nr,nc=r0,comps[0][1]*0 + c0 if False else (r0,comps[0][2] and rel and (0,0))[0]
            nr,nc=r0,rel and rel[0][1] or 0
            nr,nc=r0,r0 and 0
            nr,nc=r0,c0 if False else (r0,rel and rel[0][1] or 0)
            nr,nc=r0,c0= r0,rel and rel[0][1] or 0
            nr,nc=r0,c0
            nr,nc=r0,r0*0+rel[0][1] if rel else (r0,0)
            nr,nc=r0,c0
            nr,nc=r0,r0*0+comps[0][1]*0+rel and rel[0][1] or 0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,r0 and 0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,(comps[0][2] and comps[0][2][0][1]) if comps[0][2] else 0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=(r0,rel and rel[0][1] or 0)
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=r0,c0
            nr,nc=(r0,c0)
            new_r,new_c=r0,c0
        else:
            pr,pc,_,ph0,pw0=comps[idx-1]
            new_r=pr+ph0
            new_c=pc+pw0
            comps[idx]=(new_r,col,rel,ph,pw)
        for dx,dy in rel:
            x=new_r+dx; y=new_c+dy
            if 0<=x<h and 0<=y<len0:
                out[x][y]=col
        prev=(new_r,new_c,ph,pw)
    return out