def solve(grid):
    from collections import deque, Counter
    h, w = len(grid), len(grid[0])
    counts = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v:
                counts[v] = counts.get(v, 0) + 1
    c = max(counts, key=counts.get)
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == c and not seen[i][j]:
                q = deque([(i, j)])
                seen[i][j] = True
                comp = []
                while q:
                    x, y = q.popleft()
                    comp.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] == c:
                            seen[nx][ny] = True
                            q.append((nx, ny))
                comps.append(comp)
    def canonical(comp):
        xs = [x for x,y in comp]; ys = [y for x,y in comp]
        mi, mj = min(xs), min(ys)
        coords = [(x-mi, y-mj) for x,y in comp]
        H = max(x for x,y in coords) + 1
        W = max(y for x,y in coords) + 1
        best = None
        for _ in range(4):
            norm = tuple(sorted(coords))
            if best is None or norm < best:
                best = norm
            coords = [(y, H-1-x) for x,y in coords]
            H, W = W, H
        return best
    ids = [canonical(comp) for comp in comps]
    freq = Counter(ids)
    target = max(freq, key=lambda k: (freq[k], -len(k)))
    coords = target
    H = max(x for x,y in coords) + 1
    W = max(y for x,y in coords) + 1
    out = [[0]*W for _ in range(H)]
    for x,y in coords:
        out[x][y] = c
    return out