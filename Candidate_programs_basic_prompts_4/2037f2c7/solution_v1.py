def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                q = [(i,j)]
                visited[i][j] = True
                cells = []
                mi, ma, mj, mj2 = i, i, j, j
                for x,y in q:
                    cells.append((x,y))
                    mi = min(mi, x); ma = max(ma, x)
                    mj = min(mj, y); mj2 = max(mj2, y)
                    for dx,dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] != 0:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                clusters.append((mi,ma,mj,mj2))
    # choose cluster with minimal width, tie break by topmost
    best = min(clusters, key=lambda b: (b[3]-b[2]+1, b[0]))
    mi,ma,mj,mj2 = best
    bh, bw = ma-mi+1, mj2-mj+1
    block = [row[mj:mj2+1] for row in grid[mi:ma+1]]
    out = [[8 if block[i][j]>0 else 0 for j in range(bw)] for i in range(bh)]
    # remove all-zero rows at top and bottom
    while len(out)>0 and all(v==0 for v in out[0]):
        out.pop(0)
    while len(out)>0 and all(v==0 for v in out[-1]):
        out.pop()
    # remove duplicate consecutive rows
    ro = [out[0]] if out else []
    for r in out[1:]:
        if r != ro[-1]:
            ro.append(r)
    out = ro
    # remove all-zero cols at left and right
    if out:
        bw = len(out[0])
        left = 0
        while left<bw and all(row[left]==0 for row in out):
            left+=1
        right = bw-1
        while right>=0 and all(row[right]==0 for row in out):
            right-=1
        out = [row[left:right+1] for row in out]
    return out