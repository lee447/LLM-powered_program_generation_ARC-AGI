def solve(grid):
    h, w = len(grid), len(grid[0])
    from collections import Counter, deque
    cnt = Counter(c for row in grid for c in row if c)
    bg = max(cnt, key=lambda x: cnt[x])
    vis = [[0]*w for _ in range(h)]
    def neighbors(r,c):
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0<=nr<h and 0<=nc<w:
                yield nr, nc
    clusters = []
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c and c!=bg and not vis[i][j]:
                q = deque([(i,j)])
                vis[i][j]=1
                cells = [(i,j)]
                while q:
                    r,c0 = q.popleft()
                    for nr,nc in neighbors(r,c0):
                        if not vis[nr][nc] and grid[nr][nc]==c0 and grid[nr][nc]!=bg:
                            vis[nr][nc]=1
                            q.append((nr,nc))
                            cells.append((nr,nc))
                rs = [r for r,_ in cells]; cs = [c0 for _,c0 in cells]
                clusters.append((min(rs),cells,grid[cells[0][0]][cells[0][1]]))
    clusters.sort(key=lambda x: x[0])
    out = [row[:] for row in grid]
    brs = [i for i in range(h) if any(grid[i][j]==bg for j in range(w))]
    brow = min(brs)
    colc = min(j for j in range(w) if any(grid[i][j]==bg for i in range(h)))
    top = min(r for r,_,_ in clusters)
    for r0, cells, c in clusters:
        dy = brow - top
        for r,c0 in cells:
            nr, nc = r+dy, c0 - min(cc for _,cc,_ in clusters) + colc
            if 0<=nr<h and 0<=nc<w:
                out[nr][nc] = c
    return out