def solve(grid):
    H, W = len(grid), len(grid[0])
    # identify marker region
    mr = 0
    while mr < H and any(grid[mr][c] != 0 for c in range(W)):
        mr += 1
    color_row = grid[0]
    shape_rows = list(range(1, mr))
    # find column blocks from shape rows
    mask = [any(grid[r][c] != 0 for r in shape_rows) for c in range(W)]
    blocks = []
    c = 0
    while c < W:
        if mask[c]:
            s = c
            while c + 1 < W and mask[c + 1]:
                c += 1
            blocks.append((s, c))
        c += 1
    # find grey clusters by rows
    grey_rows = [r for r in range(H) if any(grid[r][c] == 5 for c in range(W))]
    clusters = []
    cur = []
    for r in grey_rows:
        if not cur or r == cur[-1] + 1:
            cur.append(r)
        else:
            clusters.append(cur)
            cur = [r]
    if cur:
        clusters.append(cur)
    # prepare output size
    sh = len(shape_rows)
    nb = len(blocks)
    vb = len(clusters)
    outH = vb * sh + (vb - 1)
    sw = blocks[0][1] - blocks[0][0] + 1
    outW = nb * sw + (nb - 1)
    out = [[0] * outW for _ in range(outH)]
    # extract mask from marker region
    mask2 = [[1 if grid[r][c] != 0 else 0 for c in range(blocks[b][0], blocks[b][1] + 1)] for b in range(nb) for r in shape_rows]
    mask2 = [mask2[i*sh:(i+1)*sh] for i in range(nb)]
    for bi, (cs, ce) in enumerate(blocks):
        # marker color
        mc = 0
        for x in range(cs - 1, -1, -1):
            if color_row[x] != 0:
                mc = color_row[x]
                break
        for vi, crow in enumerate(clusters):
            # overlay
            for r in crow:
                for c in range(cs, ce + 1):
                    if grid[r][c] not in (0, 5):
                        oc = grid[r][c]
                        rr = vi * (sh + 1) + (r - crow[0])
                        cc = bi * (sw + 1) + (c - cs)
                        out[rr][cc] = oc
            for dy in range(sh):
                for dx in range(sw):
                    if mask2[bi][dy][dx] and out[vi*(sh+1)+dy][bi*(sw+1)+dx] == 0:
                        out[vi*(sh+1)+dy][bi*(sw+1)+dx] = mc
    return out