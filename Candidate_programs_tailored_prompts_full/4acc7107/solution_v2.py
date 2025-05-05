def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    from collections import deque
    # collect positions by color
    pos = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v:
                pos.setdefault(v, []).append((r,c))
    # find clusters
    clusters = {}
    for v, pts in pos.items():
        spts = set(pts)
        visited = set()
        cls = []
        for p in pts:
            if p in visited: continue
            q = deque([p])
            comp = []
            visited.add(p)
            while q:
                x,y = q.popleft()
                comp.append((x,y))
                for dx,dy in dirs:
                    nx,ny = x+dx, y+dy
                    if (nx,ny) in spts and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        q.append((nx,ny))
            cls.append(comp)
        clusters[v] = cls
    # prepare output
    out = [[0]*W for _ in range(H)]
    for v, cls in clusters.items():
        # compute min/max rows
        info = []
        for comp in cls:
            rs = [p[0] for p in comp]
            info.append((max(rs), min(rs), comp))
        # sort by max row descending
        info.sort(reverse=True, key=lambda x: (x[0], x[1]))
        # bottom and top
        max_b, min_b, comp_b = info[0]
        max_t, min_t, comp_t = info[1]
        # shifts
        shift_b = (H-1) - max_b
        new_min_b = min_b + shift_b
        shift_t = new_min_b - 2 - max_t
        # apply bottom
        for r,c in comp_b:
            nr, nc = r+shift_b, c
            out[nr][nc] = v
        # apply top
        for r,c in comp_t:
            nr, nc = r+shift_t, c
            out[nr][nc] = v
    return out