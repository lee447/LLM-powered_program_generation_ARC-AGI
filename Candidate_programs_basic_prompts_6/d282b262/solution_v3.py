def solve(grid):
    h, w = len(grid), len(grid[0])
    cid = [[-1]*w for _ in range(h)]
    clusters = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and cid[i][j] < 0:
                k = len(clusters)
                clusters.append([])
                stack = [(i,j)]
                cid[i][j] = k
                while stack:
                    r,c = stack.pop()
                    clusters[k].append((r,c))
                    for dr,dc in dirs:
                        rr,cc = r+dr, c+dc
                        if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] != 0 and cid[rr][cc] < 0:
                            cid[rr][cc] = k
                            stack.append((rr,cc))
    n = len(clusters)
    rmin = [min(r for r,c in cl) for cl in clusters]
    rmax = [max(r for r,c in cl) for cl in clusters]
    adj = [[] for _ in range(n)]
    for a in range(n):
        for b in range(a+1,n):
            if not (rmax[a] < rmin[b] or rmax[b] < rmin[a]):
                adj[a].append(b)
                adj[b].append(a)
    seen = [False]*n
    groups = []
    for i in range(n):
        if not seen[i]:
            stack = [i]
            seen[i] = True
            grp = []
            while stack:
                u = stack.pop()
                grp.append(u)
                for v in adj[u]:
                    if not seen[v]:
                        seen[v] = True
                        stack.append(v)
            groups.append(grp)
    out = [[0]*w for _ in range(h)]
    for grp in groups:
        rows = set()
        for k in grp:
            rows |= set(r for r,c in clusters[k])
        if not rows:
            continue
        row_list = sorted(rows)
        maxc = 0
        for r in row_list:
            s = [grid[r][c] for c in range(w) if grid[r][c]!=0 and cid[r][c] in grp]
            maxc = max(maxc, len(s))
        start = w - maxc
        for r in row_list:
            s = [grid[r][c] for c in range(w) if grid[r][c]!=0 and cid[r][c] in grp]
            for k,v in enumerate(s):
                out[r][start+k] = v
    return out