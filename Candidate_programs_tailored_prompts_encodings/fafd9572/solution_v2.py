def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    motifs = []
    for r in range(h):
        for c in range(w):
            if grid[r][c]==1 and not visited[r][c]:
                stack = [(r,c)]
                comp = []
                visited[r][c]=True
                while stack:
                    i,j = stack.pop()
                    comp.append((i,j))
                    for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni, nj = i+di, j+dj
                        if 0<=ni<h and 0<=nj<w and not visited[ni][nj] and grid[ni][nj]==1:
                            visited[ni][nj]=True
                            stack.append((ni,nj))
                if comp:
                    motifs.append(comp)
    pivots = []
    for comp in motifs:
        minr = min(r for r,c in comp)
        minc = min(c for r,c in comp)
        if (minr,minc) in comp and (minr,minc+1) in comp and (minr+1,minc) in comp:
            piv = (minr,minc)
        else:
            piv = min(comp)
        pivots.append((piv, comp))
    new = [row[:] for row in grid]
    if len(pivots)==6:
        colors = []
        for i in range(h):
            for j in range(w):
                v = grid[i][j]
                if v not in (0,1) and v not in colors:
                    colors.append(v)
        c1, c2 = colors[0], colors[1]
        for (r,c), comp in pivots:
            col = c1 if r==c else c2
            for i,j in comp:
                new[i][j] = col
    else:
        anchor = []
        for r in range(h):
            for c in range(w):
                if grid[r][c] not in (0,1):
                    anchor.append((r,c,grid[r][c]))
        anchor.sort(key=lambda x:(x[0],x[1]))
        pivots.sort(key=lambda x:(x[0][0],x[0][1]))
        for (p,comp),(ar,ac,av) in zip(pivots,anchor):
            for i,j in comp:
                new[i][j] = av
    return new