from collections import deque
def solve(grid):
    h,w=len(grid),len(grid[0])
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    visited=[[False]*w for _ in range(h)]
    clusters=[]
    for y in range(h):
        for x in range(w):
            if grid[y][x]==2 and not visited[y][x]:
                pts=[]
                dq=deque([(y,x)])
                visited[y][x]=True
                while dq:
                    cy,cx=dq.popleft()
                    pts.append((cy,cx))
                    for dy,dx in dirs:
                        ny,nx=cy+dy,cx+dx
                        if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and grid[ny][nx]==2:
                            visited[ny][nx]=True
                            dq.append((ny,nx))
                clusters.append(pts)
    cluster_boundaries=[]
    for pts in clusters:
        b=set()
        for y,x in pts:
            for dy,dx in dirs:
                ny,nx=y+dy,x+dx
                if 0<=ny<h and 0<=nx<w and grid[ny][nx]==7:
                    b.add((ny,nx))
        cluster_boundaries.append(b)
    network={(y,x) for y in range(h) for x in range(w) if grid[y][x]==6}
    connected=[False]*len(clusters)
    while True:
        best=None
        choice=None
        for i,boundary in enumerate(cluster_boundaries):
            if connected[i]: continue
            dq=deque()
            prev={}
            for y,x in network:
                dq.append((y,x))
                prev[(y,x)]=None
            found=None
            while dq and found is None:
                cy,cx=dq.popleft()
                if (cy,cx) in boundary:
                    found=(cy,cx)
                    break
                for dy,dx in dirs:
                    ny,nx=cy+dy,cx+dx
                    if 0<=ny<h and 0<=nx<w and (ny,nx) not in prev and grid[ny][nx]!=2:
                        prev[(ny,nx)]=(cy,cx)
                        dq.append((ny,nx))
            if found is None: continue
            path=[]
            cur=found
            while cur is not None:
                path.append(cur)
                cur=prev[cur]
            path=path[::-1]
            dist=len(path)-1
            if best is None or dist<best:
                best=dist
                choice=(i,path)
        if choice is None:
            break
        i,path=choice
        for y,x in path:
            if grid[y][x]==7:
                grid[y][x]=6
            network.add((y,x))
        connected[i]=True
    return grid