def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = {'E':(0,1),'W':(0,-1),'N':(-1,0),'S':(1,0)}
    # find all 3-clusters
    visited = [[False]*W for _ in range(H)]
    clusters = []
    for r in range(H):
        for c in range(W):
            if grid[r][c]==3 and not visited[r][c]:
                # bfs
                stack = [(r,c)]
                comp = []
                visited[r][c] = True
                for x,y in stack:
                    comp.append((x,y))
                    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr,nc = x+dr, y+dc
                        if 0<=nr<H and 0<=nc<W and not visited[nr][nc] and grid[nr][nc]==3:
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                # bounding box
                rs = [p[0] for p in comp]; cs = [p[1] for p in comp]
                r0,r1 = min(rs), max(rs)
                c0,c1 = min(cs), max(cs)
                clusters.append((comp, r0, r1, c0, c1))
    # try all assignments
    nd = len(clusters)
    best = None
    # require distinct directions
    from itertools import product
    for choice in product(('E','N','W','S'), repeat=nd):
        if len(set(choice))!=nd: continue
        newcells = []
        ok = True
        for i,(comp,r0,r1,c0,c1) in enumerate(clusters):
            d = choice[i]
            dr,dc = dirs[d]
            bh = r1-r0+1; bw = c1-c0+1
            if d=='E': shift = (0, bw+1)
            elif d=='W': shift = (0, -(bw+1))
            elif d=='S': shift = (bh+1, 0)
            else: shift = (-(bh+1), 0)
            for (r,c) in comp:
                nr, nc = r+shift[0], c+shift[1]
                if not (0<=nr<H and 0<=nc<W) or grid[nr][nc]!=0:
                    ok = False; break
                newcells.append((nr,nc,d))
            if not ok:
                newcells = []; break
        if ok:
            best = newcells
            break
    out = [row[:] for row in grid]
    if best:
        for nr,nc,d in best:
            col = 1 if d in ('E','W') else 8
            out[nr][nc] = col
    return out