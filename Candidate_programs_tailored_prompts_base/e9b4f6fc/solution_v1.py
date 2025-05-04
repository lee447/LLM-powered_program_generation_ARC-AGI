def solve(grid: list[list[int]]) -> list[list[int]]:
    R, C = len(grid), len(grid[0])
    visited = [[False]*C for _ in range(R)]
    clusters = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0 and not visited[i][j]:
                col = grid[i][j]
                q = [(i,j)]
                visited[i][j] = True
                comp = [(i,j)]
                for x,y in q:
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and grid[nx][ny]==col:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                clusters.append((col, comp))
    frame_comp = None
    best = -1
    for col, comp in clusters:
        rs = [r for r,_ in comp]; cs = [c for _,c in comp]
        r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
        h, w = r1-r0+1, c1-c0+1
        perim = 2*(h+w)-4
        if h>=2 and w>=2 and len(comp)==perim and len(comp)>best:
            best = len(comp)
            frame_comp = comp
    region_set = set(frame_comp)
    q = list(frame_comp)
    for x,y in q:
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0<=nx<R and 0<=ny<C and (nx,ny) not in region_set and grid[nx][ny]!=0:
                region_set.add((nx,ny))
                q.append((nx,ny))
    rs = [r for r,_ in region_set]; cs = [c for _,c in region_set]
    r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
    anchors = []
    seen = set()
    for i in range(R):
        for j in range(C):
            if (i,j) not in region_set and grid[i][j]!=0:
                for dx,dy in ((0,1),(1,0)):
                    ni, nj = i+dx, j+dy
                    if 0<=ni<R and 0<=nj<C and (ni,nj) not in region_set and grid[ni][nj]!=0:
                        pair = frozenset((grid[i][j],grid[ni][nj]))
                        if pair not in seen:
                            seen.add(pair)
                            anchors.append((grid[i][j],grid[ni][nj]))
    region_colors = {grid[i][j] for i in range(r0,r1+1) for j in range(c0,c1+1)}
    mapping = {}
    for a,b in anchors:
        ina = a in region_colors; inb = b in region_colors
        if ina ^ inb:
            if ina:
                mapping[a] = b
            else:
                mapping[b] = a
    out = []
    for i in range(r0,r1+1):
        row = []
        for j in range(c0,c1+1):
            v = grid[i][j]
            row.append(mapping.get(v, v))
        out.append(row)
    return out