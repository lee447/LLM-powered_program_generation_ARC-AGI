def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            k = grid[i][j]
            if k > 1 and not visited[i][j]:
                stack = [(i, j)]
                comp = []
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
                            if grid[nr][nc] == 1 or grid[nr][nc] == k:
                                visited[nr][nc] = True
                                stack.append((nr, nc))
                rs = [r for r,c in comp]
                cs = [c for r,c in comp]
                rmin, rmax = min(rs), max(rs)
                cmin, cmax = min(cs), max(cs)
                if rmax - rmin >= 2 and cmax - cmin >= 2:
                    for r in range(rmin+1, rmax):
                        for c in range(cmin+1, cmax):
                            if (r, c) in comp and out[r][c] == 1:
                                out[r][c] = k
    return out