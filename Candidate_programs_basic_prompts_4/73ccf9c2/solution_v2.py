def solve(grid):
    from collections import deque
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    seen = [[False]*w for _ in range(h)]
    clusters = []
    color = None
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0:
                color = grid[i][j]
                break
        if color is not None:
            break
    for i in range(h):
        for j in range(w):
            if not seen[i][j] and grid[i][j] == color:
                q = deque([(i,j)])
                seen[i][j] = True
                comp = []
                while q:
                    x,y = q.popleft()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not seen[nx][ny] and grid[nx][ny] == color:
                            seen[nx][ny] = True
                            q.append((nx,ny))
                clusters.append(comp)
    def median(lst):
        s = sorted(lst)
        n = len(s)
        return s[n//2]
    delta_sets = []
    for comp in clusters:
        rows = [x for x,y in comp]
        cols = [y for x,y in comp]
        mr = median(rows)
        mc = median(cols)
        ds = set((x-mr, y-mc) for x,y in comp)
        delta_sets.append(ds)
    core = delta_sets[0]
    for ds in delta_sets[1:]:
        core = core & ds
    if not core:
        core = delta_sets[0]
    rs = [r for r,c in core]
    cs = [c for r,c in core]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    H, W = r1-r0+1, c1-c0+1
    out = [[0]*W for _ in range(H)]
    for r,c in core:
        out[r-r0][c-c0] = color
    return out