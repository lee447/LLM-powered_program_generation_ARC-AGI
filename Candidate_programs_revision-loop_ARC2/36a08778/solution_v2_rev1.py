from collections import deque
def solve(grid):
    h,w=len(grid),len(grid[0])
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    seen=[[False]*w for _ in range(h)]
    clusters2=[]
    for y in range(h):
        for x in range(w):
            if grid[y][x]==2 and not seen[y][x]:
                q=deque([(x,y)]); seen[y][x]=True; pts=[(x,y)]
                while q:
                    cx,cy=q.popleft()
                    for dx,dy in dirs:
                        nx,ny=cx+dx,cy+dy
                        if 0<=nx<w and 0<=ny<h and not seen[ny][nx] and grid[ny][nx]==2:
                            seen[ny][nx]=True; q.append((nx,ny)); pts.append((nx,ny))
                boundary=set()
                for cx,cy in pts:
                    for dx,dy in dirs:
                        nx,ny=cx+dx,cy+dy
                        if 0<=nx<w and 0<=ny<h and grid[ny][nx]==7:
                            boundary.add((nx,ny))
                clusters2.append(boundary)
    network=set((x,y) for y in range(h) for x in range(w) if grid[y][x]==6)
    unconnected=list(range(len(clusters2)))
    while unconnected:
        best=None; best_path=None; best_i=None
        for i in unconnected:
            boundary=clusters2[i]
            q=deque(); parent={}
            for p in network:
                q.append(p); parent[p]=None
            found=None
            while q and found is None:
                u=q.popleft()
                if u in boundary:
                    found=u; break
                ux,uy=u
                for dx,dy in dirs:
                    vx,vy=ux+dx,uy+dy
                    if 0<=vx<w and 0<=vy<h and (vx,vy) not in parent and grid[vy][vx]!=2:
                        parent[(vx,vy)]=(ux,uy); q.append((vx,vy))
            if found is None: continue
            path=[]
            cur=found
            while parent[cur] is not None:
                path.append(cur)
                cur=parent[cur]
            path.reverse()
            if best is None or len(path)<best:
                best=len(path); best_path=path; best_i=i
        if best_path is None:
            break
        for x,y in best_path:
            if grid[y][x]==7:
                grid[y][x]=6
            network.add((x,y))
        unconnected.remove(best_i)
    return grid