from collections import deque, defaultdict

def solve(grid):
    n, m = len(grid), len(grid[0])
    vis = [[False]*m for _ in range(n)]
    comps = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0 and not vis[i][j]:
                q = deque([(i, j)])
                vis[i][j] = True
                cells = []
                while q:
                    x, y = q.popleft()
                    cells.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 0 and not vis[nx][ny]:
                            vis[nx][ny] = True
                            q.append((nx, ny))
                rs = [x for x, y in cells]
                cs = [y for x, y in cells]
                r0, r1 = min(rs), max(rs)
                c0, c1 = min(cs), max(cs)
                h, w = r1-r0+1, c1-c0+1
                patch = tuple(tuple(grid[r0+i][c0+j] for j in range(w)) for i in range(h))
                comps.append((patch, r0, c0, len(cells)))
    patterns = defaultdict(list)
    for patch, r0, c0, size in comps:
        if size > 1:
            patterns[patch].append((r0, c0))
    out = [[0]*m for _ in range(n)]
    for patch, lst in patterns.items():
        if len(lst) > 1:
            h, w = len(patch), len(patch[0])
            for r0, c0 in lst:
                for i in range(h):
                    for j in range(w):
                        v = patch[i][j]
                        if v != 0:
                            out[r0+i][c0+j] = v
    return out