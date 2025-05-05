def solve(grid):
    R, C = len(grid), len(grid[0])
    frames = []
    for c in range(1, 10):
        pts = [(r, cc) for r in range(R) for cc in range(C) if grid[r][cc] == c]
        if not pts:
            continue
        minr = min(r for r, _ in pts)
        maxr = max(r for r, _ in pts)
        minc = min(cc for _, cc in pts)
        maxc = max(cc for _, cc in pts)
        h = maxr - minr + 1
        w = maxc - minc + 1
        if h < 3 or w < 3:
            continue
        ok = True
        for cc in range(minc, maxc + 1):
            if grid[minr][cc] != c or grid[maxr][cc] != c:
                ok = False
                break
        if not ok:
            continue
        for rr in range(minr, maxr + 1):
            if grid[rr][minc] != c or grid[rr][maxc] != c:
                ok = False
                break
        if ok:
            frames.append((h * w, minr, maxr, minc, maxc))
    if frames:
        _, minr, maxr, minc, maxc = max(frames, key=lambda x: x[0])
    else:
        vis = [[False] * C for _ in range(R)]
        comps = []
        for r in range(R):
            for cc in range(C):
                if grid[r][cc] != 0 and not vis[r][cc]:
                    stack = [(r, cc)]
                    vis[r][cc] = True
                    comp = [(r, cc)]
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < R and 0 <= ny < C and not vis[nx][ny] and grid[nx][ny] != 0:
                                vis[nx][ny] = True
                                stack.append((nx, ny))
                                comp.append((nx, ny))
                    rs = [p[0] for p in comp]
                    cs = [p[1] for p in comp]
                    mr, MR = min(rs), max(rs)
                    mc, MC = min(cs), max(cs)
                    area = (MR - mr + 1) * (MC - mc + 1)
                    if area == len(comp):
                        comps.append((area, mr, MR, mc, MC))
        _, minr, maxr, minc, maxc = max(comps, key=lambda x: x[0])
    mapping = {}
    for r in range(R):
        for cc in range(C - 1):
            if grid[r][cc] != 0 and grid[r][cc + 1] != 0:
                if not (minr <= r <= maxr and minc <= cc <= maxc) and not (minr <= r <= maxr and minc <= cc + 1 <= maxc):
                    mapping[grid[r][cc + 1]] = grid[r][cc]
    out = [[grid[r][cc] for cc in range(minc, maxc + 1)] for r in range(minr, maxr + 1)]
    H, W = len(out), len(out[0])
    for i in range(H):
        for j in range(W):
            v = out[i][j]
            if v in mapping:
                out[i][j] = mapping[v]
    return out