def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 6 and not seen[i][j]:
                stack = [(i,j)]
                comp = []
                seen[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and grid[nr][nc]==6:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                comps.append(comp)
    for comp in comps:
        if len(comp)!=3: continue
        comp_set = set(comp)
        center = None
        for r,c in comp:
            cnt = 0
            nbrs = []
            for dr,dc in dirs:
                if (r+dr, c+dc) in comp_set:
                    cnt += 1
                    nbrs.append((r+dr, c+dc))
            if cnt==2:
                center = (r,c)
                neigh = nbrs
                break
        if center is None: continue
        (r0,c0) = center
        v1 = (neigh[0][0]-r0, neigh[0][1]-c0)
        v2 = (neigh[1][0]-r0, neigh[1][1]-c0)
        if abs(v1[0])+abs(v1[1])!=1 or abs(v2[0])+abs(v2[1])!=1 or v1[0]*v2[0]+v1[1]*v2[1]!=0:
            continue
        for i,j in ((1,1),(2,0),(0,2),(2,1),(1,2)):
            nr = r0 + i*v1[0] + j*v2[0]
            nc = c0 + i*v1[1] + j*v2[1]
            if 0<=nr<h and 0<=nc<w and grid[nr][nc]!=6:
                out[nr][nc] = 4
    return out