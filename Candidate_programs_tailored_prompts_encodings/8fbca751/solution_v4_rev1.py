def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 8 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                cluster = []
                while stack:
                    r, c = stack.pop()
                    cluster.append((r, c))
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if dr == 0 and dc == 0: continue
                            rr, cc = r+dr, c+dc
                            if 0 <= rr < h and 0 <= cc < w and not visited[rr][cc] and grid[rr][cc] == 8:
                                visited[rr][cc] = True
                                stack.append((rr, cc))
                rs = [r for r, c in cluster]
                cs = [c for r, c in cluster]
                rmin, rmax = min(rs), max(rs)
                cmin, cmax = min(cs), max(cs)
                for rr in range(rmin, rmax+1):
                    for cc in range(cmin, cmax+1):
                        if grid[rr][cc] == 0:
                            grid[rr][cc] = 2
    return grid