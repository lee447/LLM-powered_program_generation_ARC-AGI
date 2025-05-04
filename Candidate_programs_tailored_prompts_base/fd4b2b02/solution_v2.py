def solve(grid):
    H = len(grid)
    W = len(grid[0])
    min_r, min_c, max_r, max_c = H, W, -1, -1
    for r in range(H):
        for c in range(W):
            if grid[r][c] != 0:
                if r < min_r: min_r = r
                if r > max_r: max_r = r
                if c < min_c: min_c = c
                if c > max_c: max_c = c
    h = max_r - min_r + 1
    w = max_c - min_c + 1
    orig_color = grid[min_r][min_c]
    comp = {3: 6, 6: 3}.get(orig_color, orig_color)
    mask = [[1 if grid[min_r + dr][min_c + dc] == orig_color else 0 for dc in range(w)] for dr in range(h)]
    rh, rw = w, h
    rot = [[mask[h - 1 - dc][dr] for dc in range(h)] for dr in range(w)]
    out = [[0] * W for _ in range(H)]
    edges = [
        ((W - w) // 2, 0),
        ((W - w) // 2, H - h),
        (0, (H - h) // 2),
        (W - w, (H - h) // 2)
    ]
    for x0, y0 in edges:
        for dr in range(h):
            for dc in range(w):
                if mask[dr][dc]:
                    out[y0 + dr][x0 + dc] = orig_color
    for qx in (0, W // 2):
        for qy in (0, H // 2):
            x0 = qx + (W // 2 - rw) // 2
            y0 = qy + (H // 2 - rh) // 2
            for dr in range(rh):
                for dc in range(rw):
                    if rot[dr][dc]:
                        out[y0 + dr][x0 + dc] = comp
    return out