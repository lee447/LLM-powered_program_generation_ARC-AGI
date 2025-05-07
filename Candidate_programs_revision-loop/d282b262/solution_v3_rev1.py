def solve(grid):
    h, w = len(grid), len(grid[0])
    vis = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not vis[i][j]:
                q = [(i,j)]
                vis[i][j] = True
                pts = [(i,j)]
                for x,y in q:
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 0 and not vis[nx][ny]:
                            vis[nx][ny] = True
                            q.append((nx,ny))
                            pts.append((nx,ny))
                rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                pat = [[grid[r][c] for c in range(c0, c1+1)] for r in range(r0, r1+1)]
                clusters.append({'r0':r0,'h':r1-r0+1,'c0':c0,'w':c1-c0+1,'pat':pat})
    n = len(clusters)
    adj = {i:[] for i in range(n)}
    for i in range(n):
        for j in range(i+1,n):
            a=clusters[i]; b=clusters[j]
            if a['r0'] < b['r0']+b['h'] and b['r0'] < a['r0']+a['h']:
                adj[i].append(j); adj[j].append(i)
    out = [[0]*w for _ in range(h)]
    seen = set()
    for i in range(n):
        if i in seen: continue
        comp = []
        stack = [i]; seen.add(i)
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); stack.append(v)
        comp_sorted = sorted(comp, key=lambda u: clusters[u]['c0'])
        color = {}
        for u in comp_sorted:
            if u not in color:
                color[u] = 0
                q = [u]
                for x in q:
                    for y in adj[x]:
                        if y in comp and y not in color:
                            color[y] = 1-color[x]
                            q.append(y)
        min_r = min(clusters[u]['r0'] for u in comp)
        max_r1 = max(clusters[u]['r0']+clusters[u]['h'] for u in comp)
        max_total = 0
        for r in range(min_r, max_r1):
            s = 0
            for u in comp:
                if clusters[u]['r0'] <= r < clusters[u]['r0']+clusters[u]['h']:
                    s += clusters[u]['w']
            if s > max_total: max_total = s
        pos_start = w - max_total
        widths0 = max(clusters[u]['w'] for u in comp if color[u]==0)
        slot_pos = {0: pos_start, 1: pos_start + widths0}
        for u in comp:
            nc = slot_pos[color[u]]
            r0 = clusters[u]['r0']
            for dr in range(clusters[u]['h']):
                for dc in range(clusters[u]['w']):
                    out[r0+dr][nc+dc] = clusters[u]['pat'][dr][dc]
    return out