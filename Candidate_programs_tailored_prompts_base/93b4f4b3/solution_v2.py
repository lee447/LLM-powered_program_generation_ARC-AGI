def solve(grid):
    H, W = len(grid), len(grid[0])
    C = grid[0][0]
    stripe_w = next(j for j in range(W) if grid[0][j] != C)
    anchors = [r for r in range(H) if all(grid[r][j] == C for j in range(stripe_w))]
    bands = []
    for i in range(len(anchors)-1):
        r0, r1 = anchors[i]+1, anchors[i+1]
        bands.append(list(range(r0, r1)))
    clusters = []
    for band in bands:
        cells = [(r, c) for r in band for c in range(stripe_w, W) if grid[r][c] != 0]
        rs = [r for r,_ in cells]; cs = [c for _,c in cells]
        r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
        shape = []
        color = grid[cells[0][0]][cells[0][1]]
        for r, c in cells:
            shape.append((r - r0, c - c0))
        clusters.append((shape, color, r1-r0+1, c1-c0+1))
    bh = len(bands[0])
    if bh % 2 == 0:
        new_clusters = clusters[1:] + clusters[:1]
    else:
        new_clusters = clusters[::-1]
    out = [[0]*stripe_w for _ in range(H)]
    for r in range(H):
        if r in anchors:
            out[r] = [C]*stripe_w
        else:
            out[r] = [C]*stripe_w
            for i, band in enumerate(bands):
                if r in band:
                    shape, color, sh, sw = new_clusters[i]
                    start_c = (stripe_w - sw)//2
                    for dr, dc in shape:
                        if band[0] + dr == r:
                            out[r][start_c + dc] = color
                    break
    return out