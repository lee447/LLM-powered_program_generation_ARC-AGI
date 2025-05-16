import sys
def solve(grid):
    h=len(grid);w=len(grid[0])
    vis=[[False]*w for _ in range(h)]
    frames=[]
    for i in range(h):
        for j in range(w):
            if not vis[i][j]:
                c=grid[i][j]
                pts=[]
                stack=[(i,j)]
                vis[i][j]=True
                while stack:
                    x,y=stack.pop()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny]=True
                            stack.append((nx,ny))
                if len(pts)<4: continue
                rs=[p[0] for p in pts]; cs=[p[1] for p in pts]
                r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
                height=r1-r0+1; width=maxc-minc+1
                per=2*(height+width)-4
                if len(pts)!=per: continue
                ok=True
                for x,y in pts:
                    if not (x==r0 or x==r1 or y==minc or y==maxc):
                        ok=False;break
                if ok:
                    frames.append((height*width,c,r0,r1,minc,maxc))
    if not frames: return grid
    _,fc,r0,r1,c0,c1=min(frames,key=lambda x:x[0])
    out=[]
    for i in range(r0,r1+1):
        row=[]
        for j in range(c0,c1+1):
            v=grid[i][j]
            row.append(3 if v==fc else v)
        out.append(row)
    return out