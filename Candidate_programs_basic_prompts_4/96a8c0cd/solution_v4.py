def solve(grid):
    from collections import deque
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    # find start
    for i in range(h):
        for j in range(w):
            if g[i][j] == 2:
                start = (i, j)
    # find clusters of 1 or 3
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if not seen[i][j] and g[i][j] in (1,3):
                col = g[i][j]
                q = [(i,j)]
                seen[i][j] = True
                pts = []
                mi, ma = i, i
                mj, na = j, j
                qi = 0
                while qi < len(q):
                    r,c = q[qi]; qi+=1
                    pts.append((r,c))
                    mi = min(mi, r); ma = max(ma, r)
                    mj = min(mj, c); na = max(na, c)
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not seen[nr][nc] and g[nr][nc]==col:
                            seen[nr][nc]=True
                            q.append((nr,nc))
                clusters.append((mj, pts, mi, ma, mj, na))
    # sort by min_col
    clusters.sort(key=lambda x: x[0])
    # BFS function
    def bfs(s, t):
        q = deque([s])
        prev = {s:None}
        while q:
            r,c = q.popleft()
            if (r,c)==t:
                break
            for dr,dc in ((0,1),(1,0),(0,-1),(-1,0)):
                nr, nc = r+dr, c+dc
                if 0<=nr<h and 0<=nc<w and (nr,nc) not in prev:
                    if (nr,nc)==t or grid[nr][nc]==0:
                        prev[(nr,nc)] = (r,c)
                        q.append((nr,nc))
        if t not in prev:
            return []
        path = []
        cur = t
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        return path[::-1]
    cur = start
    # connect clusters
    for _, pts, r0, r1, c0, c1 in clusters:
        # gather candidates
        cand = []
        spts = set(pts)
        for r,c in pts:
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc = r+dr, c+dc
                if 0<=nr<h and 0<=nc<w and grid[nr][nc]==0:
                    cand.append((nr,nc))
        cand = list(set(cand))
        # pick nearest by manhattan
        cand.sort(key=lambda x:(abs(x[0]-cur[0])+abs(x[1]-cur[1]), x[0], x[1]))
        tgt = cand[0]
        path = bfs(cur, tgt)
        for r,c in path[1:]:
            if g[r][c]==0:
                g[r][c]=2
        cur = tgt
    # extend to border
    # find any border cell
    borders = [(i,j) for i in (0,h-1) for j in range(w)] + [(i,j) for i in range(h) for j in (0,w-1)]
    dist = {}
    q = deque([cur]); dist[cur]=None
    end = None
    while q:
        x = q.popleft()
        if x in borders:
            end = x; break
        r,c = x
        for dr,dc in ((0,1),(1,0),(0,-1),(-1,0)):
            nr,nc = r+dr, c+dc
            if 0<=nr<h and 0<=nc<w and (nr,nc) not in dist:
                if grid[nr][nc]==0:
                    dist[(nr,nc)] = x
                    q.append((nr,nc))
                elif (nr,nc) in borders:
                    dist[(nr,nc)] = x
                    end = (nr,nc)
                    q.clear()
                    break
    if end:
        path = []
        curp = end
        while curp is not None:
            path.append(curp)
            curp = dist[curp]
        for r,c in path[::-1][1:]:
            if g[r][c]==0:
                g[r][c]=2
    return g