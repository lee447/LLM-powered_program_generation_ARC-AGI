def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs8 = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    fives = {(r,c) for r in range(h) for c in range(w) if grid[r][c]==5}
    adj = {p:[] for p in fives}
    for r,c in fives:
        for dr,dc in dirs8:
            nr,nc = r+dr, c+dc
            if (nr,nc) in fives:
                adj[(r,c)].append((nr,nc))
    ends = [p for p,nei in adj.items() if len(nei)==1]
    from collections import deque
    def bfs(a):
        dist = {a:0}
        dq = deque([a])
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    dq.append(v)
        return dist
    best = (None,None,-1)
    for i in range(len(ends)):
        for j in range(i+1,len(ends)):
            a, b = ends[i], ends[j]
            d = bfs(a).get(b, -1)
            if d > best[2]:
                best = (a, b, d)
    a, b = best[0], best[1]
    def get_cluster(p):
        for dr,dc in dirs8:
            nr,nc = p[0]+dr, p[1]+dc
            if 0<=nr<h and 0<=nc<w and grid[nr][nc] not in (0,5):
                col = grid[nr][nc]
                vis = set()
                stk = [(nr,nc)]
                vis.add((nr,nc))
                while stk:
                    x,y = stk.pop()
                    for dr2,dc2 in dirs8:
                        xx,yy = x+dr2, y+dc2
                        if 0<=xx<h and 0<=yy<w and (xx,yy) not in vis and grid[xx][yy]==col:
                            vis.add((xx,yy))
                            stk.append((xx,yy))
                return col, vis
        return None, set()
    ca, ca_cells = get_cluster(a)
    cb, cb_cells = get_cluster(b)
    def center(cells):
        rs = [r for r,c in cells]
        cs = [c for r,c in cells]
        return ((min(rs)+max(rs))//2, (min(cs)+max(cs))//2)
    ar,ac = center(ca_cells)
    br,bc = center(cb_cells)
    va = grid[ar][ac]
    vb = grid[br][bc]
    out = [[0]*w for _ in range(h)]
    for r,c in fives:
        out[r][c] = 5
    for r,c in ca_cells:
        if (r,c)==(ar,ac):
            out[r][c] = vb
        else:
            out[r][c] = ca
    for r,c in cb_cells:
        if (r,c)==(br,bc):
            out[r][c] = va
        else:
            out[r][c] = cb
    return out