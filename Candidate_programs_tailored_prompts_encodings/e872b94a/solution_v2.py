def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    def bfs(sr, sc):
        comp = [(sr, sc)]
        visited[sr][sc] = True
        queue = [(sr, sc)]
        while queue:
            r, c = queue.pop()
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == 5:
                    visited[nr][nc] = True
                    comp.append((nr, nc))
                    queue.append((nr, nc))
        return comp
    count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not visited[i][j]:
                comp = bfs(i, j)
                rs = [r for r,c in comp]
                cs = [c for r,c in comp]
                rmin, rmax = min(rs), max(rs)
                cmin, cmax = min(cs), max(cs)
                if len(comp) == 4 and rmax - rmin == 2 and cmax - cmin == 1:
                    count += 1
                elif cmax == cmin and rmax - rmin + 1 == len(comp) and len(comp) >= 2:
                    count += 1
    return [[0] for _ in range(count)]