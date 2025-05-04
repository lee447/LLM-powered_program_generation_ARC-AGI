def solve(grid):
    h = len(grid)
    w = len(grid[0])
    stripes = []
    for x in range(w):
        ys = [y for y in range(h) if grid[y][x] != 0]
        if ys and min(ys) == 0 and max(ys) == h - 1:
            cols = {grid[y][x] for y in ys}
            if len(cols) == 1:
                stripes.append(x)
    stripes.sort()
    stripe_colors = []
    for x in stripes:
        for y in range(h):
            if grid[y][x] != 0:
                stripe_colors.append(grid[y][x])
                break
    all_colors = {grid[y][x] for y in range(h) for x in range(w)}
    shape_color = next(c for c in all_colors if c != 0 and c not in stripe_colors)
    shape = [[grid[y][x] == shape_color for x in range(w)] for y in range(h)]
    x_adj = {x: set() for x in range(w)}
    xs = sorted({x for y in range(h) for x in range(w) if shape[y][x]})
    for y in range(h):
        run = []
        for x in range(w):
            if shape[y][x]:
                run.append(x)
            else:
                if run:
                    for i in range(len(run) - 1):
                        x1, x2 = run[i], run[i + 1]
                        if x2 == x1 + 1:
                            x_adj[x1].add(x2)
                            x_adj[x2].add(x1)
                    run = []
        if run:
            for i in range(len(run) - 1):
                x1, x2 = run[i], run[i + 1]
                if x2 == x1 + 1:
                    x_adj[x1].add(x2)
                    x_adj[x2].add(x1)
    visited = set()
    segments = []
    for x in xs:
        if x not in visited:
            comp = []
            stack = [x]
            visited.add(x)
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in x_adj[u]:
                    if v not in visited:
                        visited.add(v)
                        stack.append(v)
            comp.sort()
            segments.append(comp)
    target_seg_count = len(stripes)
    while len(segments) < target_seg_count:
        segments.sort(key=lambda seg: (-len(seg), seg[0]))
        seg = segments.pop(0)
        run_len = {x: sum(shape[y][x] for y in range(h)) for x in seg}
        m = min(run_len.values())
        M = [x for x in seg if run_len[x] == m]
        M.sort()
        # find first contiguous interval in M
        block = []
        start = M[0]
        prev = M[0]
        block = [start]
        for x in M[1:]:
            if x == prev + 1:
                block.append(x)
            else:
                break
            prev = x
        seg2 = [x for x in seg if x not in block]
        segments.append(sorted(seg2))
        segments.append(block)
    segments.sort(key=lambda seg: seg[0])
    mapping = {}
    for i, seg in enumerate(segments):
        c = stripe_colors[i]
        for x in seg:
            mapping[x] = c
    out = [[0]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if grid[y][x] == shape_color:
                out[y][x] = mapping[x]
    return out