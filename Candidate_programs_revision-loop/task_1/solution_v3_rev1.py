from collections import deque, defaultdict

def solve(grid):
    n, m = len(grid), len(grid[0])
    vis = [[False]*m for _ in range(n)]
    dims2comps = defaultdict(list)
    intact = defaultdict(list)
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
                dims2comps[(h, w)].append((r0, c0))
                if len(cells) == h*w:
                    intact[(h, w)].append((r0, c0))
    prototypes = {}
    for d, lst in intact.items():
        if len(lst) >= 1 and len(dims2comps[d]) > 1:
            r0, c0 = lst[0]
            h, w = d
            prototypes[d] = [row[c0:c0+w] for row in grid[r0:r0+h]]
    out = [[0]*m for _ in range(n)]
    for d, positions in dims2comps.items():
        if d in prototypes:
            patch = prototypes[d]
            h, w = d
            for r0, c0 in positions:
                for i in range(h):
                    for j in range(w):
                        out[r0+i][c0+j] = patch[i][j]
    return out