from collections import deque
def solve(grid):
    h,w=len(grid),len(grid[0])
    vis=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==3 and not vis[i][j]:
                q=deque([(i,j)]);vis[i][j]=True;cells=[(i,j)]
                while q:
                    x,y=q.popleft()
                    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==3:
                            vis[nx][ny]=True;q.append((nx,ny));cells.append((nx,ny))
                rs=[x for x,y in cells];cs=[y for x,y in cells]
                r0,r1,c0,c1=min(rs),max(rs),min(cs),max(cs)
                hh,ww=r1-r0+1,c1-c0+1
                if hh%2==1 and ww%2==1:
                    mask=[[grid[r0+ii][c0+jj]==3 for jj in range(ww)] for ii in range(hh)]
                    comps.append((hh*ww,r0,c0,hh,ww,mask))
    comps.sort(key=lambda x:x[0],reverse=True)
    out=[row[:] for row in grid]
    if len(comps)>=1:
        _,r0,c0,hh,ww,mask=comps[0]
        tr,tc=r0,c0+ww+1
        for i in range(hh):
            for j in range(ww):
                if mask[i][j] and 0<=tr+i<h and 0<=tc+j<w:
                    out[tr+i][tc+j]=1
    if len(comps)>=2:
        _,r0_1,c0_1,hh1,ww1,mask1=comps[1]
        _,r0_0,c0_0,hh0,ww0,_=comps[0]
        tr,tc=r0_0+hh0+1,c0_0+ww0-1
        for i in range(hh1):
            for j in range(ww1):
                if mask1[i][j] and 0<=tr+i<h and 0<=tc+j<w:
                    out[tr+i][tc+j]=8
    return out