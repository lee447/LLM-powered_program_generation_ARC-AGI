def solve(grid):
    from collections import Counter, deque
    n, m = len(grid), len(grid[0])
    cnt = Counter(c for row in grid for c in row)
    bg = max(cnt, key=lambda c: cnt[c])
    colors = [c for c in cnt if c != bg]
    # find block color A = color with largest bounding box
    def bounds(c):
        r0, r1, c0, c1 = n, -1, m, -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == c:
                    r0, r1 = min(r0, i), max(r1, i)
                    c0, c1 = min(c0, j), max(c1, j)
        return (r0, r1, c0, c1)
    bboxes = {c: bounds(c) for c in colors}
    areas = {c: (bboxes[c][1]-bboxes[c][0]+1)*(bboxes[c][3]-bboxes[c][2]+1) for c in colors}
    A = max(colors, key=lambda c: areas[c])
    r0, r1, c0, c1 = bboxes[A]
    bh, bw = r1-r0+1, c1-c0+1
    # compute vertical step
    ys = sorted({bounds[A][0] for _ in [0]})
    xs = sorted({bboxes[A][2]})
    # find all A tops
    tops = []
    for i in range(n-bh+1):
        for j in range(m-bw+1):
            ok = True
            for di in range(bh):
                for dj in range(bw):
                    if grid[i+di][j+dj] == A:
                        continue
                    if grid[i+di][j+dj] != bg:
                        ok = False; break
                if not ok: break
            if ok:
                # check full A block
                full = all(grid[i+di][j+dj] == A for di in range(bh) for dj in range(bw))
                if full: tops.append((i,j))
    if len(tops) >= 2:
        ys = sorted(set(i for i,j in tops))
        xs = sorted(set(j for i,j in tops))
        if len(ys) > 1:
            step_y = ys[1]-ys[0]
        else:
            step_y = bh + (n - (ys[0]+bh))//1
        if len(xs) > 1:
            step_x = xs[1]-xs[0]
        else:
            step_x = bw + (m - (xs[0]+bw))//1
        origin_y = ys[0]
        origin_x = xs[0]
    else:
        origin_y, origin_x = r0, c0
        step_y, step_x = bh*2, bw*2
    # fill color B
    B = [c for c in colors if c != A][0] if len(colors)>1 else A
    out = [row[:] for row in grid]
    for i in range(origin_y, n, step_y):
        for j in range(origin_x, m, step_x):
            # skip if this block has any A
            foundA = any(0<=i+di<n and 0<=j+dj<m and out[i+di][j+dj]==A for di in range(bh) for dj in range(bw))
            if not foundA and i+bh<=n and j+bw<=m:
                for di in range(bh):
                    for dj in range(bw):
                        out[i+di][j+dj] = B
    return out