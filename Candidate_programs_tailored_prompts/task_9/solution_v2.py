def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    vis = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not vis[i][j]:
                stack = [(i,j)]
                vis[i][j] = True
                comp = []
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not vis[nr][nc] and grid[nr][nc] == 5:
                            vis[nr][nc] = True
                            stack.append((nr,nc))
                comps.append(comp)
    for comp in comps:
        rs = [r for r,c in comp]
        cs = [c for r,c in comp]
        min_r, max_r, min_c, max_c = min(rs), max(rs), min(cs), max(cs)
        top = all(grid[min_r][c] == 5 for c in range(min_c, max_c+1))
        bot = all(grid[max_r][c] == 5 for c in range(min_c, max_c+1))
        upright = bot and not top
        stripe_r = min_r-1 if upright else max_r+1
        start_c, end_c = min_c+1, max_c
        if 0 <= stripe_r < h:
            for c in range(start_c, end_c):
                if 0 <= c < w:
                    out[stripe_r][c] = 2
        if max_r - min_r == 3 and max_c - min_c == 3:
            for r in range(min_r+1, min_r+3):
                for c in range(min_c+1, min_c+3):
                    out[r][c] = 2
    return out