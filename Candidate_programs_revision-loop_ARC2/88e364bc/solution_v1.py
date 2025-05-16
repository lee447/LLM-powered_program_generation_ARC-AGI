def solve(grid):
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    from collections import deque
    visited = [[False]*w for _ in range(h)]
    q = deque()
    for i in range(h):
        for j in range(w):
            if (i==0 or j==0 or i==h-1 or j==w-1) and grid[i][j]==0 and not visited[i][j]:
                visited[i][j] = True
                q.append((i,j))
    while q:
        i,j = q.popleft()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = i+di, j+dj
            if 0<=ni<h and 0<=nj<w and not visited[ni][nj] and grid[ni][nj]==0:
                visited[ni][nj] = True
                q.append((ni,nj))
    holes = {(i,j) for i in range(h) for j in range(w) if grid[i][j]==0 and not visited[i][j]}
    comps = []
    seen = set()
    for cell in holes:
        if cell in seen: continue
        comp = []
        dq = deque([cell])
        seen.add(cell)
        while dq:
            x,y = dq.popleft()
            comp.append((x,y))
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny = x+dx, y+dy
                if (nx,ny) in holes and (nx,ny) not in seen:
                    seen.add((nx,ny))
                    dq.append((nx,ny))
        comps.append(comp)
    out = [row[:] for row in grid]
    for comp in comps:
        has4 = any(grid[i][j]==4 for i,j in comp)
        if not has4: continue
        neigh = {pos:[] for pos in comp}
        s = set(comp)
        for i,j in comp:
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = i+di, j+dj
                if (ni,nj) in s:
                    neigh[(i,j)].append((ni,nj))
        # prune leaves
        deg = {p:len(neigh[p]) for p in neigh}
        leafq = deque(p for p in deg if deg[p]==1)
        while leafq:
            leaf = leafq.popleft()
            if deg.get(leaf,0)!=1: continue
            for nb in neigh[leaf]:
                neigh[nb].remove(leaf)
                deg[nb] -= 1
                if deg[nb]==1:
                    leafq.append(nb)
            del neigh[leaf]
            deg[leaf] = 0
        if not neigh: continue
        # build cycle path
        start = next(iter(neigh))
        path = [start]
        prev = None
        cur = start
        while True:
            nxts = [p for p in neigh[cur] if p!=prev]
            if not nxts: break
            nxt = nxts[0]
            if nxt==start: break
            path.append(nxt)
            prev, cur = cur, nxt
        pathlen = len(path)
        old4 = [p for p in path if grid[p[0]][p[1]]==4]
        new4 = [path[(path.index(p)+1)%pathlen] for p in old4]
        for i,j in old4:
            out[i][j] = 0
        for i,j in new4:
            out[i][j] = 4
    return out