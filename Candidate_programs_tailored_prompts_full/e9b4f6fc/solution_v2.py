def solve(grid):
    R, C = len(grid), len(grid[0])
    vis = [[False]*C for _ in range(R)]
    frames = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] != 0 and not vis[r][c]:
                col = grid[r][c]
                stack = [(r, c)]
                vis[r][c] = True
                comp = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < R and 0 <= ny < C and not vis[nx][ny] and grid[nx][ny] == col:
                            vis[nx][ny] = True
                            stack.append((nx, ny))
                            comp.append((nx, ny))
                rows = [p[0] for p in comp]
                cols = [p[1] for p in comp]
                minr, maxr = min(rows), max(rows)
                minc, maxc = min(cols), max(cols)
                w, h = maxc-minc+1, maxr-minr+1
                if w > 1 and h > 1 and len(comp) == 2*(w+h)-4:
                    frames.append((col, minr, maxr, minc, maxc))
    col, minr, maxr, minc, maxc = max(frames, key=lambda f:(f[2]-f[1]+1)*(f[4]-f[3]+1))
    mapping = {}
    for r in range(R):
        for c in range(C-1):
            inside1 = minr <= r <= maxr and minc <= c <= maxc
            inside2 = minr <= r <= maxr and minc <= c+1 <= maxc
            if not inside1 and not inside2 and grid[r][c] != 0 and grid[r][c+1] != 0:
                mapping[grid[r][c+1]] = grid[r][c]
    h, w = maxr-minr+1, maxc-minc+1
    out = [[grid[r][c] for c in range(minc, maxc+1)] for r in range(minr, maxr+1)]
    for i in range(h):
        for j in range(w):
            if i and j and i < h-1 and j < w-1:
                v = out[i][j]
                if v in mapping:
                    out[i][j] = mapping[v]
    return out