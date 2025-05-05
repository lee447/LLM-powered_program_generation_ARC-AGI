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
    segs0 = []
    in_seg = False
    curr_start = curr_len = 0
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
                if curr_len >= 2:
                    segs0.append(curr_start)
                in_seg = False
            curr_len = 0
    if in_seg and curr_len >= 2:
        segs0.append(curr_start)
    if not segs0:
        return [[0]*W for _ in range(H)]
    r0 = segs0[0]
    H0 = 0
    for r in range(r0, H):
        if row_has_cluster(r, 2):
            H0 += 1
        else:
            break
    good = [True]*W
    for dr in range(H0):
        row = grid[r0+dr]
        for c in range(W):
            if row[c] == 0:
                good[c] = False
    blocks = []
    c = 0
    while c < W:
        if good[c]:
            start = c
            while c < W and good[c]:
                c += 1
            blocks.append((start, c-start))
        else:
            c += 1
    if not blocks:
        return [[0]*W for _ in range(H)]
    b0_start, b0_w = blocks[0]
    proto = [[grid[r0+dr][b0_start+dc] for dc in range(b0_w)] for dr in range(H0)]
    segs = []
    in_seg = False
    curr_start = curr_len = 0
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
    out = [[0]*W for _ in range(H)]
    for start in segs:
        for dr in range(H0):
            r = start + dr
            if r < H:
                for bs, _ in blocks:
                    for dc in range(b0_w):
                        v = proto[dr][dc]
                        if v != 0:
                            out[r][bs+dc] = v
    return out