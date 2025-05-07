def solve(grid):
    from collections import deque
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
            if not seen[i][j] and grid[i][j]==c:
                q = deque([(i,j)])
                seen[i][j] = True
                comp = []
                while q:
                    x,y = q.popleft()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not seen[nx][ny] and grid[nx][ny]==c:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                comps.append(comp)
    max_len = max(len(comp) for comp in comps)
    cand = [comp for comp in comps if len(comp)*2 >= max_len]
    best = None
    best_area = None
    for comp in cand:
        xs = [x for x,y in comp]
        ys = [y for x,y in comp]
        mi, ma = min(xs), max(xs)
        mj, mb = min(ys), max(ys)
        area = (ma-mi+1)*(mb-mj+1)
        if best_area is None or area < best_area:
            best_area = area
            best = (comp, mi, ma, mj, mb)
    comp, mi, ma, mj, mb = best
    H, W = ma-mi+1, mb-mj+1
    base = [[0]*W for _ in range(H)]
    for x,y in comp:
        base[x-mi][y-mj] = c
    def rot(mat):
        H1, W1 = len(mat), len(mat[0])
        R = [[0]*H1 for _ in range(W1)]
        for i in range(H1):
            for j in range(W1):
                R[j][H1-1-i] = mat[i][j]
        return R
    variants = []
    m = base
    for _ in range(4):
        variants.append(m)
        m = rot(m)
    best_mat = min(variants, key=lambda m: tuple(x for row in m for x in row))
    return best_mat