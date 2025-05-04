def solve(grid):
    H, W = len(grid), len(grid[0])
    border_row = border_col = None
    for r in range(1, H-1):
        v = grid[r][0]
        if all(grid[r][c] == v for c in range(W)) and grid[r-1][0] != v and grid[r+1][0] == v:
            border_row = r
            break
    if border_row is None:
        for c in range(1, W-1):
            v = grid[0][c]
            if all(grid[r][c] == v for r in range(H)) and grid[0][c-1] != v and grid[0][c+1] == v:
                border_col = c
                break
    def zone_color_at(r, c):
        if border_row is not None:
            return grid[0][c] if r < border_row else grid[-1][c]
        else:
            return grid[r][0] if c < border_col else grid[r][-1]
    base = [[zone_color_at(r, c) if grid[r][c] == 2 else grid[r][c] for c in range(W)] for r in range(H)]
    res = [row[:] for row in base]
    vis = [[False]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 2 and not vis[i][j]:
                stack = [(i,j)]
                comp = []
                vis[i][j] = True
                while stack:
                    r,c = stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == 2 and not vis[nr][nc]:
                            vis[nr][nc] = True
                            stack.append((nr,nc))
                rows = [r for r,c in comp]
                cols = [c for r,c in comp]
                rmin, rmax, cmin, cmax = min(rows), max(rows), min(cols), max(cols)
                zc = zone_color_at(rmin, cmin)
                if zc == 1:
                    delta = W-1 - cmax
                else:
                    delta = 0 - cmin
                for r,c in comp:
                    res[r][c+delta] = 2
    return res