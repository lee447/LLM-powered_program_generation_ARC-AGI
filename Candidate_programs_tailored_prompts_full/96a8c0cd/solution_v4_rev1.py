import heapq

def solve(grid):
    H, W = len(grid), len(grid[0])
    seed = None
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 2:
                seed = (i, j)
                break
        if seed: break

    segs = []
    for i in range(H):
        for j in range(W - 2):
            v = grid[i][j]
            if v in (1, 3) and grid[i][j+1] == v and grid[i][j+2] == v:
                segs.append([(i, j), (i, j+1), (i, j+2)])
    for i in range(H - 2):
        for j in range(W):
            v = grid[i][j]
            if v in (1, 3) and grid[i+1][j] == v and grid[i+2][j] == v:
                segs.append([(i, j), (i+1, j), (i+2, j)])

    centers = set()
    for pts in segs:
        pts = sorted(pts)
        if pts[0][0] == pts[1][0]:
            r = pts[0][0]
            cs = sorted(p[1] for p in pts)
            centers.add((r, cs[1]))
        else:
            c = pts[0][1]
            rs = sorted(p[0] for p in pts)
            centers.add((rs[1], c))

    points = [seed] + list(centers)
    n = len(points)
    dist = [float('inf')] * n
    used = [False] * n
    parent = [-1] * n
    dist[0] = 0
    pq = [(0, 0)]
    while pq:
        d, u = heapq.heappop(pq)
        if used[u]: continue
        used[u] = True
        for v in range(n):
            if used[v]: continue
            d2 = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
            if d2 < dist[v]:
                dist[v] = d2
                parent[v] = u
                heapq.heappush(pq, (d2, v))

    out = [row[:] for row in grid]
    for v in range(1, n):
        u = parent[v]
        r1, c1 = points[u]
        r2, c2 = points[v]
        for c in range(min(c1, c2), max(c1, c2) + 1):
            if out[r1][c] == 0 and c not in (c1, c2):
                out[r1][c] = 2
        for r in range(min(r1, r2), max(r1, r2) + 1):
            if out[r][c2] == 0 and r not in (r1, r2):
                out[r][c2] = 2

    return out