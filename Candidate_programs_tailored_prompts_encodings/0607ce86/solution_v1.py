def solve(grid):
    H = len(grid)
    W = len(grid[0]) if H else 0
    def row_has_cluster(r, minlen):
        cnt = 0
        for c in range(W):
            if grid[r][c] != 0:
                cnt += 1
            else:
                if cnt >= minlen:
                    return True
                cnt = 0
        return cnt >= minlen
    # find prototype start row r0
    r0 = None
    for r in range(H):
        # header row: cluster of non-zero length>=2
        cnt = 0
        ok = False
        for c in range(W):
            if grid[r][c] != 0:
                cnt += 1
            else:
                if cnt >= 2:
                    ok = True
                    break
                cnt = 0
        if cnt >= 2: ok = True
        if ok:
            r0 = r
            break
    if r0 is None:
        return [[0]*W for _ in range(H)]
    # compute prototype height H0
    H0 = 0
    for r in range(r0, H):
        if row_has_cluster(r, 2):
            H0 += 1
        else:
            break
    # find header blocks at r0
    blocks = []
    c = 0
    while c < W:
        if grid[r0][c] != 0:
            start = c
            while c < W and grid[r0][c] != 0:
                c += 1
            blocks.append((start, c - start))
        else:
            c += 1
    # build prototype
    proto = [[0]*W for _ in range(H0)]
    for dr in range(H0):
        r = r0 + dr
        for start, width in blocks:
            for c in range(start, start+width):
                proto[dr][c] = grid[r][c]
    # find segment groups
    segs = []
    in_seg = False
    curr_start = 0
    curr_len = 0
    for r in range(H):
        if row_has_cluster(r, 2):
            if not in_seg:
                in_seg = True
                curr_start = r
                curr_len = 1
            else:
                curr_len += 1
        else:
            if in_seg:
                if curr_len >= H0:
                    segs.append(curr_start)
                in_seg = False
            curr_len = 0
    if in_seg and curr_len >= H0:
        segs.append(curr_start)
    # build output
    out = [[0]*W for _ in range(H)]
    for start in segs:
        for dr in range(H0):
            r = start + dr
            if r < H:
                for c in range(W):
                    v = proto[dr][c]
                    if v != 0:
                        out[r][c] = v
    return out