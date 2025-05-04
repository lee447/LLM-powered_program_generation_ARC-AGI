def solve(grid):
    h, w = len(grid), len(grid[0])
    c = next(grid[i][j] for i in range(h) for j in range(w) if grid[i][j] != 0)
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == c and not seen[i][j]:
                q = [(i,j)]
                seen[i][j] = True
                pts = []
                while q:
                    x,y = q.pop()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] == c:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                clusters.append(pts)
    shapes = []
    for pts in clusters:
        rs = [p[0] for p in pts]; cs = [p[1] for p in pts]
        r0,r1 = min(rs), max(rs); c0,c1 = min(cs), max(cs)
        shapes.append([[1 if grid[r][c]==c else 0 for c in range(c0,c1+1)] for r in range(r0,r1+1)])
    min_h = min(len(s) for s in shapes)
    min_w = min(len(s[0]) for s in shapes)
    def rot90(m):
        H,W = len(m), len(m[0])
        return [[m[H-1-r][c] for r in range(H)] for c in range(W)]
    def submats(m):
        H,W = len(m), len(m[0])
        for i in range(H-min_h+1):
            for j in range(W-min_w+1):
                yield tuple(tuple(m[i+di][j+dj] for dj in range(min_w)) for di in range(min_h))
    candidate_sets = []
    for s in shapes:
        rots = [s]
        for _ in range(3):
            rots.append(rot90(rots[-1]))
        cand = set()
        for r in rots:
            for sm in submats(r):
                cand.add(sm)
        candidate_sets.append(cand)
    common = set.intersection(*candidate_sets)
    pat = [list(row) for row in common.pop()]
    return pat