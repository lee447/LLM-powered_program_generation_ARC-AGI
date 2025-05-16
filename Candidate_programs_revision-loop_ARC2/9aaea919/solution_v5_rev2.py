from collections import deque, defaultdict
def solve(grid):
    h, w = len(grid), len(grid[0])
    freq = {}
    for row in grid:
        for v in row:
            freq[v] = freq.get(v, 0) + 1
    bg = max(freq, key=freq.get)
    visited = [[False]*w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != bg and not visited[i][j]:
                col = grid[i][j]
                q = deque([(i, j)])
                visited[i][j] = True
                cells = []
                while q:
                    x, y = q.popleft()
                    cells.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == col:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                ys = [y for _, y in cells]
                xs = [x for x, _ in cells]
                cx = sum(ys) / len(ys)
                cy = sum(xs) / len(xs)
                clusters.append({'cells': cells, 'col': col, 'cx': cx, 'cy': cy})
    groups = defaultdict(list)
    for c in clusters:
        key = int(round(c['cx']))
        groups[key].append(c)
    out = [row[:] for row in grid]
    for grp in groups.values():
        if len(grp) > 1:
            grp.sort(key=lambda c: c['cy'])
            n = len(grp)
            for i, c in enumerate(grp):
                src = grp[(i+1) % n]
                for x, y in c['cells']:
                    out[x][y] = src['col']
    return out