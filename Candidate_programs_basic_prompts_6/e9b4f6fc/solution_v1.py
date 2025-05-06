def solve(grid):
    H, W = len(grid), len(grid[0])
    coords = {}
    for i in range(H):
        for j in range(W):
            v = grid[i][j]
            if v > 0:
                coords.setdefault(v, []).append((i, j))
    best_c, best_area, best_box = None, 0, None
    for c, pts in coords.items():
        rs = [p[0] for p in pts]
        cs = [p[1] for p in pts]
        r1, r2, c1, c2 = min(rs), max(rs), min(cs), max(cs)
        area = (r2 - r1 + 1) * (c2 - c1 + 1)
        if area > best_area:
            best_area = area
            best_c = c
            best_box = (r1, r2, c1, c2)
    r1, r2, c1, c2 = best_box
    cropped = [row[c1:c2+1] for row in grid[r1:r2+1]]
    mh, mw = r2-r1+1, c2-c1+1
    visited = [[False]*W for _ in range(H)]
    mapping = {}
    for i in range(H):
        for j in range(W):
            if r1 <= i <= r2 and c1 <= j <= c2: continue
            if grid[i][j] == 0 or visited[i][j]: continue
            for di,dj in ((0,1),(1,0)):
                ni, nj = i+di, j+dj
                if 0 <= ni < H and 0 <= nj < W and not (r1 <= ni <= r2 and c1 <= nj <= c2) and grid[ni][nj] > 0 and not visited[ni][nj]:
                    new, old = grid[i][j], grid[ni][nj]
                    mapping[old] = new
                    visited[i][j] = visited[ni][nj] = True
                    break
    out = [[0]*mw for _ in range(mh)]
    for i in range(mh):
        for j in range(mw):
            v = cropped[i][j]
            if i==0 or i==mh-1 or j==0 or j==mw-1:
                out[i][j] = v
            else:
                out[i][j] = mapping.get(v, v)
    return out