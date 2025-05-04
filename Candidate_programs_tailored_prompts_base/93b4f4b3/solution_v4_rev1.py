def solve(grid):
    H, W = len(grid), len(grid[0])
    C = grid[0][0]
    stripe_w = next(j for j in range(W) if grid[0][j] != C)
    anchors = [r for r in range(H) if all(grid[r][j] == C for j in range(stripe_w))]
    bands = [list(range(anchors[i] + 1, anchors[i + 1])) for i in range(len(anchors) - 1)]
    clusters = []
    for band in bands:
        cells = [(r, c) for r in band for c in range(stripe_w, W) if grid[r][c] != 0]
        rs = [r for r, _ in cells]; cs = [c for _, c in cells]
        r0, r1 = min(rs), max(rs); c0, c1 = min(cs), max(cs)
        shape = [(r - r0, c - c0) for r, c in cells]
        color = grid[cells[0][0]][cells[0][1]]
        clusters.append((shape, color, r1 - r0 + 1, c1 - c0 + 1))
    bh = len(bands[0])
    if bh % 2 == 0:
        new_clusters = clusters[1:] + clusters[:1]
    else:
        new_clusters = clusters[::-1]
    out = [[C] * stripe_w for _ in range(H)]
    for band, (shape, color, _, sw) in zip(bands, new_clusters):
        avg_dc = sum(dc for dr, dc in shape) / len(shape)
        thr = (sw - 1) / 2
        start = (stripe_w - sw) // 2 + (1 if avg_dc > thr else 0)
        for dr, dc in shape:
            out[band[0] + dr][start + dc] = color
    return out