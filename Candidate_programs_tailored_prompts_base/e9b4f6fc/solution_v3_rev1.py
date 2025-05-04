from collections import deque
def solve(grid):
    R, C = len(grid), len(grid[0])
    vis = [[False]*C for _ in range(R)]
    best_comp = []
    for i in range(R):
        for j in range(C):
            if grid[i][j]!=0 and not vis[i][j]:
                q = deque([(i,j)])
                vis[i][j]=True
                comp = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx,y+dy
                        if 0<=nx<R and 0<=ny<C and not vis[nx][ny] and grid[nx][ny]!=0:
                            vis[nx][ny]=True
                            q.append((nx,ny))
                            comp.append((nx,ny))
                if len(comp)>len(best_comp):
                    best_comp=comp
    rs = [r for r,_ in best_comp]; cs = [c for _,c in best_comp]
    r0,r1,c0,c1 = min(rs),max(rs),min(cs),max(cs)
    region_area = (r1-r0+1)*(c1-c0+1)
    colors = {}
    for i in range(R):
        for j in range(C):
            v = grid[i][j]
            if v!=0:
                colors.setdefault(v,[]).append((i,j))
    best_ring_area=0
    best_ring=None
    for v,pts in colors.items():
        rows = [x for x,_ in pts]; cols = [y for _,y in pts]
        rr0,rr1,cc0,cc1 = min(rows),max(rows),min(cols),max(cols)
        h,w = rr1-rr0+1,cc1-cc0+1
        if h>=2 and w>=2:
            ok=True
            for y in range(cc0,cc1+1):
                if grid[rr0][y]!=v or grid[rr1][y]!=v:
                    ok=False; break
            if not ok: continue
            for x in range(rr0,rr1+1):
                if grid[x][cc0]!=v or grid[x][cc1]!=v:
                    ok=False; break
            if ok:
                area = h*w
                if area>best_ring_area:
                    best_ring_area=area
                    best_ring=(rr0,rr1,cc0,cc1)
    if best_ring and best_ring_area>=region_area:
        r0,r1,c0,c1 = best_ring
    region_colors = {grid[i][j] for i in range(r0,r1+1) for j in range(c0,c1+1)}
    mapping = {}
    seen = set()
    for i in range(R):
        for j in range(C):
            if not (r0<=i<=r1 and c0<=j<=c1) and grid[i][j]!=0:
                for dx,dy in ((0,1),(1,0)):
                    ni,nj = i+dx,j+dy
                    if 0<=ni<R and 0<=nj<C and not (r0<=ni<=r1 and c0<=nj<=c1) and grid[ni][nj]!=0:
                        a,b = grid[i][j],grid[ni][nj]
                        p = frozenset((a,b))
                        if p in seen: continue
                        seen.add(p)
                        ina, inb = a in region_colors, b in region_colors
                        if ina^inb:
                            if ina: mapping[a]=b
                            else: mapping[b]=a
    out = []
    for i in range(r0,r1+1):
        row = []
        for j in range(c0,c1+1):
            v = grid[i][j]
            row.append(mapping.get(v,v))
        out.append(row)
    return out