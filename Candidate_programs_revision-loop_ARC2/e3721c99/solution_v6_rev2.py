from collections import deque
def solve(grid):
    h,w=len(grid),len(grid[0])
    vis=[[False]*w for _ in range(h)]
    tops=[]
    for i in range(h):
        for j in range(w):
            if not vis[i][j] and grid[i][j] not in (0,5):
                col=grid[i][j]
                q=deque([(i,j)])
                vis[i][j]=True
                cells=[]
                while q:
                    x,y=q.popleft()
                    cells.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==col:
                            vis[nx][ny]=True
                            q.append((nx,ny))
                rs=[x for x,_ in cells]
                cs=[y for _,y in cells]
                r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
                if r1-r0+1==3:
                    tmpl=tuple(tuple(1 if grid[r0+i][minc+j]==col else 0 for j in range(maxc-minc+1)) for i in range(3))
                    tops.append((minc,maxc-minc+1,tmpl,col))
    tops.sort()
    size_to_mask={}
    size_to_colors={}
    for _,sz,tmpl,col in tops:
        size_to_mask[sz]=tmpl
        size_to_colors.setdefault(sz,[]).append(col)
    matches=[]
    for sz,tmpl in size_to_mask.items():
        th,tw=len(tmpl),len(tmpl[0])
        for i in range(h-th+1):
            for j in range(w-tw+1):
                ok=True
                for di in range(th):
                    for dj in range(tw):
                        want=tmpl[di][dj]
                        v=grid[i+di][j+dj]
                        if want:
                            if v!=5: ok=False; break
                        else:
                            if v!=0: ok=False; break
                    if not ok: break
                if ok:
                    matches.append((i,j,sz))
    matches.sort()
    out=[row[:] for row in grid]
    used={sz:0 for sz in size_to_colors}
    for i,j,sz in matches:
        cols=size_to_colors[sz]
        col=cols[used[sz]%len(cols)]
        used[sz]+=1
        tmpl=size_to_mask[sz]
        th,tw=len(tmpl),len(tmpl[0])
        for di in range(th):
            for dj in range(tw):
                if tmpl[di][dj]:
                    out[i+di][j+dj]=col
    return out