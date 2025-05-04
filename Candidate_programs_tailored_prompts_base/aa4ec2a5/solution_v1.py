def solve(grid):
    H = len(grid)
    W = len(grid[0])
    visited = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 1 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                comp = []
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and grid[nr][nc] == 1:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                comps.append(comp)
    res = [row[:] for row in grid]
    for comp in comps:
        rs = [r for r,_ in comp]; cs = [c for _,c in comp]
        min_r, max_r = min(rs), max(rs)
        min_c, max_c = min(cs), max(cs)
        for c in range(min_c-1, max_c+2):
            for r in (min_r-1, max_r+1):
                if 0 <= r < H and 0 <= c < W and grid[r][c] != 1:
                    res[r][c] = 2
        for r in range(min_r-1, max_r+2):
            for c in (min_c-1, max_c+1):
                if 0 <= r < H and 0 <= c < W and grid[r][c] != 1:
                    res[r][c] = 2
        h = max_r - min_r + 1
        w = max_c - min_c + 1
        thr_r = h // 2
        thr_c = w // 2
        for r in range(min_r, max_r+1):
            for c in range(min_c, max_c+1):
                if grid[r][c] == 4 and res[r][c] == 4:
                    if (r-min_r) < thr_r or (c-min_c) < thr_c:
                        res[r][c] = 8
                    else:
                        res[r][c] = 6
    return res