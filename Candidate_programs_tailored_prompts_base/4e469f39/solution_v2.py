def solve(grid):
    H = len(grid)
    W = len(grid[0])
    new_grid = [[0]*W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 5:
                new_grid[r][c] = 5
    visited = [[False]*W for _ in range(H)]
    comps = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 5 and not visited[r][c]:
                stack = [(r, c)]
                visited[r][c] = True
                comp = [(r, c)]
                for rr, cc in stack:
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and grid[nr][nc] == 5:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                            comp.append((nr, nc))
                comps.append(comp)
    for comp in comps:
        rs = [p[0] for p in comp]
        cs = [p[1] for p in comp]
        minr, maxr = min(rs), max(rs)
        minc, maxc = min(cs), max(cs)
        anchor = next(c for c in range(minc, maxc+1) if grid[minr][c] != 5)
        for rr in range(minr+1, maxr):
            for cc in range(minc+1, maxc):
                new_grid[rr][cc] = 2
        bar_r = minr - 1
        if bar_r >= 0:
            center = (minc + maxc) / 2.0
            if anchor < center:
                for cc in range(anchor, W):
                    if grid[bar_r][cc] == 0 and new_grid[bar_r][cc] == 0:
                        new_grid[bar_r][cc] = 2
                    else:
                        break
            else:
                for cc in range(anchor, -1, -1):
                    if grid[bar_r][cc] == 0 and new_grid[bar_r][cc] == 0:
                        new_grid[bar_r][cc] = 2
                    else:
                        break
    return new_grid