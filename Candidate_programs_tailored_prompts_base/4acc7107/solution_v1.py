def solve(grid):
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    vis = [[False]*w for _ in range(h)]
    clusters = {}
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c and not vis[i][j]:
                stack = [(i,j)]
                vis[i][j] = True
                cells = []
                while stack:
                    x,y = stack.pop()
                    cells.append((x,y))
                    for dx,dy in dirs:
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not vis[nx][ny] and grid[nx][ny]==c:
                            vis[nx][ny]=True
                            stack.append((nx,ny))
                clusters.setdefault(c, []).append(cells)
    squares = {}
    bars = {}
    for c, clist in clusters.items():
        sqs = []
        runs = []
        for cells in clist:
            s = set(cells)
            for x,y in cells:
                if (x+1,y) in s and (x,y+1) in s and (x+1,y+1) in s:
                    sqs.append([(x,y),(x+1,y),(x,y+1),(x+1,y+1)])
            # find runs of 4
            by_row = {}
            by_col = {}
            for x,y in cells:
                by_row.setdefault(x,[]).append(y)
                by_col.setdefault(y,[]).append(x)
            for x, ys in by_row.items():
                ys = sorted(ys)
                for i in range(len(ys)-3):
                    if ys[i+3]-ys[i]==3:
                        runs.append([(x,ys[i]+k) for k in range(4)])
            for y, xs in by_col.items():
                xs = sorted(xs)
                for i in range(len(xs)-3):
                    if xs[i+3]-xs[i]==3:
                        runs.append([(xs[i]+k,y) for k in range(4)])
        sq = min(sqs, key=lambda s:(min(x for x,y in s),min(y for x,y in s)))
        br = max(runs, key=lambda s:(min(x for x,y in s),min(y for x,y in s)))
        squares[c] = sq
        bars[c] = br
    items = []
    for c in squares:
        minr = min(x for x,y in squares[c])
        items.append((minr, c))
    items.sort(reverse=True)
    out = [[0]*w for _ in range(h)]
    assemblies = []
    for _,c in items:
        sq = squares[c]
        br = bars[c]
        min_sq_r = min(x for x,y in sq)
        min_sq_c = min(y for x,y in sq)
        norm_sq = [(x-min_sq_r, y-min_sq_c) for x,y in sq]
        min_br_r = min(x for x,y in br)
        min_br_c = min(y for x,y in br)
        norm_br = [(x-min_br_r, y-min_br_c) for x,y in br]
        max_sq_r = max(r for r,c2 in norm_sq)
        max_sq_c = max(c2 for r,c2 in norm_sq)
        max_br_r = max(r for r,c2 in norm_br)
        max_br_c = max(c2 for r,c2 in norm_br)
        aw = max_sq_c+1 + max_br_c+1
        ah = max(max_sq_r+1, max_br_r+1)
        assemblies.append((c, norm_sq, norm_br, ah, aw, max_sq_c+1))
    total_h = sum(a[3] for a in assemblies)
    cur = h-total_h
    for c, sq, br, ah, aw, sqw in assemblies:
        for r,c2 in sq:
            out[cur+r][c2] = c
        for r,c2 in br:
            out[cur+r][sqw+c2] = c
        cur += ah
    return out