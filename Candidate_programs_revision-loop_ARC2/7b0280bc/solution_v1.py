def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = {}
    for i in range(h):
        for j in range(w):
            counts[grid[i][j]] = counts.get(grid[i][j], 0) + 1
    bg = max(counts, key=lambda c: counts[c])
    colors = sorted(c for c in counts if c != bg)
    c1, c2, c3 = colors
    # detect open vs closed: closed if forms loop (each has >=1 cell on grid perimeter)
    perim = set()
    for x in range(w):
        perim.add((0, x)); perim.add((h-1, x))
    for y in range(h):
        perim.add((y, 0)); perim.add((y, w-1))
    touch = {c:0 for c in colors}
    for i,j in perim:
        v = grid[i][j]
        if v in touch:
            touch[v] += 1
    # if exactly two of the colors touch the perimeter => recolor those two shapes
    rec = [c for c in colors if touch[c] > 0]
    if len(rec) == 2:
        a, b = rec
        # map smaller id -> 5, larger -> 3
        m1, m2 = (5,3) if a < b else (3,5)
        out = [row[:] for row in grid]
        for i in range(h):
            for j in range(w):
                if grid[i][j] == a:
                    out[i][j] = m1
                elif grid[i][j] == b:
                    out[i][j] = m2
        return out
    # otherwise fill the wedge between the two most numerous shapes
    others = sorted(colors, key=lambda c: -counts[c])[:2]
    a, b = others
    # find all cells reachable from a and b along their paths
    vis = [[0]*w for _ in range(h)]
    from collections import deque
    for start in [(i,j) for i in range(h) for j in range(w) if grid[i][j]==a]:
        vis[start[0]][start[1]] |= 1
    for start in [(i,j) for i in range(h) for j in range(w) if grid[i][j]==b]:
        vis[start[0]][start[1]] |= 2
    q = deque()
    for i in range(h):
        for j in range(w):
            if grid[i][j] in (a,b):
                q.append((i,j))
    while q:
        i,j = q.popleft()
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = i+di, j+dj
            if 0<=ni<h and 0<=nj<w and grid[ni][nj]==bg:
                m = vis[i][j]
                if (vis[ni][nj] & m)==0:
                    vis[ni][nj] |= m
                    q.append((ni,nj))
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==bg and vis[i][j]==3:
                out[i][j] = 5 if a < b else 3
    return out