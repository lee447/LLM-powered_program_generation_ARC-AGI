def solve(grid):
    R = len(grid)
    C = len(grid[0])
    pos = {}
    for i in range(R):
        for j in range(C):
            c = grid[i][j]
            pos.setdefault(c, []).append((i, j))
    candidates = []
    for c, pts in pos.items():
        if len(pts) <= 1:
            continue
        min_r = min(i for i, _ in pts)
        max_r = max(i for i, _ in pts)
        min_c = min(j for _, j in pts)
        max_c = max(j for _, j in pts)
        h = max_r - min_r + 1
        w = max_c - min_c + 1
        if h * w == len(pts):
            candidates.append((h * w, c, min_r, max_r, min_c, max_c))
    area, mc, min_r, max_r, min_c, max_c = max(candidates)
    H = max_r - min_r + 1
    W = max_c - min_c + 1
    tile_rows = R // H
    tile_cols = C // W
    mask_ti = min_r // H
    mask_tj = min_c // W
    freq = {}
    for ti in range(tile_rows):
        sr = ti * H
        for tj in range(tile_cols):
            if ti == mask_ti and tj == mask_tj:
                continue
            sc = tj * W
            block = tuple(tuple(grid[sr + i][sc + j] for j in range(W)) for i in range(H))
            freq[block] = freq.get(block, 0) + 1
    best = max(freq.items(), key=lambda x: x[1])[0]
    return [list(row) for row in best]