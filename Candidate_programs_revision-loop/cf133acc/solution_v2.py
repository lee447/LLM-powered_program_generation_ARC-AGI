def solve(grid):
    h = len(grid)
    w = len(grid[0])
    # horizontal segment detection
    hor_segs = []
    for y in range(h):
        x = 0
        while x < w:
            if grid[y][x] != 0:
                c = grid[y][x]
                start = x
                while x + 1 < w and grid[y][x+1] == c:
                    x += 1
                end = x
                hor_segs.append((y, c, start, end))
            x += 1
    # merge horizontal segments by row,color if gap==1
    from collections import defaultdict
    hmap = defaultdict(list)
    for y, c, s, e in hor_segs:
        hmap[(y, c)].append((s, e))
    horizontal_shapes = []
    for (y, c), segs in hmap.items():
        segs.sort()
        merged = []
        i = 0
        while i < len(segs):
            s0, e0 = segs[i]
            j = i + 1
            while j < len(segs) and segs[j][0] - e0 == 2:
                e0 = segs[j][1]
                j += 1
            merged.append((s0, e0))
            i = j
        for s0, e0 in merged:
            if e0 - s0 >= 1:
                gaps = [x for x in range(s0+1, e0) if grid[y][x] == 0]
                horizontal_shapes.append({'y': y, 'c': c, 'min_x': s0, 'max_x': e0, 'gaps': gaps})
    # vertical segment detection
    ver_segs = []
    for x in range(w):
        y = 0
        while y < h:
            if grid[y][x] != 0:
                c = grid[y][x]
                start = y
                while y + 1 < h and grid[y+1][x] == c:
                    y += 1
                end = y
                ver_segs.append((x, c, start, end))
            y += 1
    # merge vertical segments by col,color if gap==1
    vmap = defaultdict(list)
    for x, c, s, e in ver_segs:
        vmap[(x, c)].append((s, e))
    vertical_shapes = []
    for (x, c), segs in vmap.items():
        segs.sort()
        merged = []
        i = 0
        while i < len(segs):
            s0, e0 = segs[i]
            j = i + 1
            while j < len(segs) and segs[j][0] - e0 == 2:
                e0 = segs[j][1]
                j += 1
            merged.append((s0, e0))
            i = j
        for s0, e0 in merged:
            vertical_shapes.append({'x': x, 'c': c, 'start_y': s0, 'end_y': e0})
    # connectors
    connectors = sorted({x for sh in horizontal_shapes for x in sh['gaps']})
    res = [[0]*w for _ in range(h)]
    for x in connectors:
        shapes = []
        for sh in horizontal_shapes:
            if x in sh['gaps']:
                shapes.append((sh['y'], sh['y'], sh['c']))
        for sh in vertical_shapes:
            if sh['x'] == x:
                shapes.append((sh['start_y'], sh['end_y'], sh['c']))
        shapes.sort(key=lambda t: t[0])
        prev = -1
        for start, end, c in shapes:
            for y in range(prev+1, end+1):
                res[y][x] = c
            prev = end
    # draw horizontal shapes
    for sh in horizontal_shapes:
        y, c, a, b = sh['y'], sh['c'], sh['min_x'], sh['max_x']
        for x in range(a, b+1):
            res[y][x] = c
    return res