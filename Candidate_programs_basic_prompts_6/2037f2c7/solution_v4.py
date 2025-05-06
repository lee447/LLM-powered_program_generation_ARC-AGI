def solve(grid):
    h, w = len(grid), len(grid[0])
    groups = []
    in_run = False
    for r in range(h):
        if any(grid[r][c] != 0 for c in range(w)):
            if not in_run:
                groups.append([r, r])
                in_run = True
            else:
                groups[-1][1] = r
        else:
            in_run = False
    blocks = []
    for r0, r1 in groups:
        cols = []
        in_c = False
        for c in range(w):
            if any(grid[r][c] != 0 for r in range(r0, r1+1)):
                if not in_c:
                    cols.append([c, c])
                    in_c = True
                else:
                    cols[-1][1] = c
            else:
                in_c = False
        for c0, c1 in cols:
            blocks.append((r0, r1, c0, c1))
    # choose the block size that repeats
    sizes = {}
    for b in blocks:
        sz = (b[1]-b[0]+1, b[3]-b[2]+1)
        sizes[sz] = sizes.get(sz, 0) + 1
    tile_h, tile_w = max(sizes, key=lambda k: sizes[k])
    # find vertical groups of tiles
    vruns = []
    ys = sorted({b[0] for b in blocks if b[1]-b[0]+1==tile_h})
    i = 0
    while i < len(ys):
        j = i
        while j+1<len(ys) and ys[j+1]==ys[j]+tile_h+1:
            j+=1
        vruns.append((ys[i], j-i+1))
        i = j+1
    hruns = []
    xs = sorted({b[2] for b in blocks if b[3]-b[2]+1==tile_w})
    i = 0
    while i < len(xs):
        j = i
        while j+1<len(xs) and xs[j+1]==xs[j]+tile_w+1:
            j+=1
        hruns.append((xs[i], j-i+1))
        i = j+1
    out = [[0]*(tile_w*len(hruns)) for _ in range(len(vruns))]
    for bi, (ry, rc) in enumerate(vruns):
        for bj, (cx, cc) in enumerate(hruns):
            r0 = ry
            c0 = cx
            m = 0
            for rr in range(r0, r0+tile_h):
                for cc2 in range(c0, c0+tile_w):
                    if grid[rr][cc2] != 0:
                        m = 1
                        break
                if m:
                    break
            if m:
                for rr in range(tile_h):
                    for cc2 in range(tile_w):
                        if grid[r0+rr][c0+cc2] != 0:
                            out[bi][bj*tile_w+cc2] = 8
    return out