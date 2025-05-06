def solve(grid):
    from collections import deque
    def bfs(sr, sc, color, vis):
        q = deque([(sr, sc)])
        pts = []
        vis.add((sr, sc))
        while q:
            r, c = q.popleft()
            pts.append((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0: continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in vis and grid[nr][nc] == color:
                        vis.add((nr, nc))
                        q.append((nr, nc))
        return pts

    def orient(hull):
        def cross(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
        pts = sorted(hull)
        lower = []
        for p in pts:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(pts):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        return lower[:-1] + upper[:-1]

    def line(a, b):
        (x0, y0), (x1, y1) = a, b
        dx, dy = abs(x1-x0), abs(y1-y0)
        x, y = x0, y0
        sx = 1 if x1 > x0 else -1
        sy = 1 if y1 > y0 else -1
        pts = []
        if dx > dy:
            err = dx//2
            while x != x1:
                pts.append((x, y))
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
            pts.append((x, y))
        else:
            err = dy//2
            while y != y1:
                pts.append((x, y))
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
            pts.append((x, y))
        return pts

    H, W = len(grid), len(grid[0])
    color = 0
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0:
                color = grid[r][c]
                break
        if color: break
    vis = set()
    clusters = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] == color and (r, c) not in vis:
                clusters.append(bfs(r, c, color, vis))
    all_pts = [p for cl in clusters for p in cl]
    hull = orient(all_pts)
    outline = set()
    for i in range(len(hull)):
        a = hull[i]
        b = hull[(i+1)%len(hull)]
        for p in line(a, b):
            outline.add(p)
    rs = [r for r,c in outline]
    cs = [c for r,c in outline]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    h, w = r1-r0+1, c1-c0+1
    out = [[0]*w for _ in range(h)]
    for r,c in outline:
        out[r-r0][c-c0] = color
    return out