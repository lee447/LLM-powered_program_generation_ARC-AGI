def solve(grid):
    n = len(grid)
    m = len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*m for _ in range(n)]
    def bfs(i,j,c):
        q = [(i,j)]
        seen[i][j] = True
        minr,maxr,minc,maxc = i,i,j,j
        for x,y in q:
            for di,dj in dirs:
                ni,nj = x+di, y+dj
                if 0<=ni<n and 0<=nj<m and not seen[ni][nj] and grid[ni][nj]==c:
                    seen[ni][nj] = True
                    q.append((ni,nj))
                    minr = min(minr,ni); maxr = max(maxr,ni)
                    minc = min(minc,nj); maxc = max(maxc,nj)
        return (c, minr, maxr, minc, maxc, len(q))
    rects = []
    for i in range(n):
        for j in range(m):
            if not seen[i][j] and grid[i][j]!=1 and grid[i][j]!=0:
                rects.append(bfs(i,j,grid[i][j]))
    rects.sort(key=lambda x: -x[5])
    c,r0,r1,c0,c1,_ = rects[0]
    h = r1-r0+1; w = c1-c0+1
    if h<w:
        size = w
        out = [[0]*size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                out[i][j] = grid[r0][c0+j]
    elif w<h:
        size = h
        out = [[0]*size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                out[i][j] = grid[r0+i][c0]
    else:
        out = [[0]*w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                out[i][j] = grid[r0+i][c0+j]
    return out