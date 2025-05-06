def solve(grid):
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0 and not visited[i][j]:
                pts = [(i, j)]
                visited[i][j] = True
                q = [(i, j)]
                while q:
                    r, c = q.pop()
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            pts.append((nr, nc))
                            q.append((nr, nc))
                if len(pts) >= 5:
                    rs = [p[0] for p in pts]
                    cs = [p[1] for p in pts]
                    r0, r1 = min(rs), max(rs)
                    c0, c1 = min(cs), max(cs)
                    h, w = r1-r0+1, c1-c0+1
                    if h*w == len(pts):
                        comps.append((h, w, r0, c0))
    from collections import defaultdict
    shapes = defaultdict(list)
    for h, w, r0, c0 in comps:
        shapes[(h, w)].append((r0, c0))
    out = [[0]*W for _ in range(H)]
    for (h, w), origins in shapes.items():
        origins.sort()
        r0, c0 = origins[0]
        tile = [row[c0:c0+w] for row in grid[r0:r0+h]]
        for r, c in origins:
            for dr in range(h):
                for dc in range(w):
                    out[r+dr][c+dc] = tile[dr][dc]
    return out