def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps1 = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 1 and not visited[r][c]:
                stack = [(r,c)]
                visited[r][c] = True
                comp = []
                while stack:
                    i,j = stack.pop()
                    comp.append((i,j))
                    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni, nj = i+di, j+dj
                        if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and grid[ni][nj] == 1:
                            visited[ni][nj] = True
                            stack.append((ni,nj))
                comps1.append(comp)
    visited = [[False]*w for _ in range(h)]
    comps_color = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] not in (0,1) and not visited[r][c]:
                stack = [(r,c)]
                visited[r][c] = True
                comp = []
                while stack:
                    i,j = stack.pop()
                    comp.append((i,j))
                    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni, nj = i+di, j+dj
                        if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and grid[ni][nj] not in (0,1):
                            visited[ni][nj] = True
                            stack.append((ni,nj))
                comps_color.append(comp)
    colors = []
    seen = set()
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v not in (0,1) and v not in seen:
                seen.add(v)
                colors.append(v)
    new = [row[:] for row in grid]
    if len(colors) == 2:
        c1, c2 = colors[0], colors[1]
        pivots = []
        for comp in comps1:
            piv = min(comp)
            pivots.append((piv, comp))
        pivots.sort(key=lambda x:(x[0][0], x[0][1]))
        bands = []
        current = []
        prev_r = None
        for p, comp in pivots:
            r,_ = p
            if prev_r is None or r - prev_r <= 1:
                current.append((p, comp))
            else:
                bands.append(current)
                current = [(p, comp)]
            prev_r = r
        if current:
            bands.append(current)
        m = len(bands)//2
        for i, band in enumerate(bands):
            band.sort(key=lambda x: x[0][1])
            n = len(band)
            for j, (p, comp) in enumerate(band):
                if i < m:
                    col = c1 if j < n//2 else c2
                elif i == m:
                    col = c2
                else:
                    col = c2 if j < n//2 else c1
                for x,y in comp:
                    new[x][y] = col
    else:
        piv1 = []
        for comp in comps1:
            piv1.append((min(comp), comp))
        piv1.sort(key=lambda x:(x[0][0], x[0][1]))
        pivc = []
        for comp in comps_color:
            pivc.append((min(comp), comp))
        pivc.sort(key=lambda x:(x[0][0], x[0][1]))
        for (p1, comp1), (pc, compc) in zip(piv1, pivc):
            pr, pc0 = pc
            col = grid[pr][pc0]
            for x,y in comp1:
                new[x][y] = col
    return new