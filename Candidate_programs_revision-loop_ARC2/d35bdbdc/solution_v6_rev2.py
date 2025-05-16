import collections
def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    fives = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==5]
    adj = {p:[] for p in fives}
    for r,c in fives:
        for dr,dc in dirs8:
            q = (r+dr,c+dc)
            if q in adj:
                adj[(r,c)].append(q)
    ends = [p for p,n in adj.items() if len(n)==1]
    def bfs_dist(a):
        dq = collections.deque([a])
        dist = {a:0}
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    dq.append(v)
        return dist
    best = (None, None, -1)
    for i in range(len(ends)):
        for j in range(i+1, len(ends)):
            a, b = ends[i], ends[j]
            d = bfs_dist(a).get(b, -1)
            if d > best[2]:
                best = (a, b, d)
    a, b, _ = best
    def get_cluster(p):
        seed = None
        for dr,dc in dirs8:
            nr, nc = p[0]+dr, p[1]+dc
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] not in (0,5):
                seed = (nr,nc)
                break
        if seed is None:
            return set()
        vis = {seed}
        dq = [seed]
        while dq:
            x,y = dq.pop()
            for dr,dc in dirs8:
                xx, yy = x+dr, y+dc
                if 0 <= xx < h and 0 <= yy < w and grid[xx][yy] not in (0,5) and (xx,yy) not in vis:
                    vis.add((xx,yy))
                    dq.append((xx,yy))
        return vis
    ca = get_cluster(a)
    cb = get_cluster(b)
    def pick(cells):
        cnt = collections.Counter(grid[r][c] for r,c in cells)
        border, _ = cnt.most_common(1)[0]
        center = None
        for col,cntv in cnt.items():
            if col != border:
                center = col
                break
        center_coord = next(((r,c) for r,c in cells if grid[r][c]==center), None)
        return border, center, center_coord
    bA, cA, pA = pick(ca)
    bB, cB, pB = pick(cb)
    out = [[0]*w for _ in range(h)]
    for r,c in fives:
        out[r][c] = 5
    for r,c in ca:
        out[r][c] = bA if (r,c)!=pA else cB
    for r,c in cb:
        out[r][c] = bB if (r,c)!=pB else cA
    return out