def solve(grid):
    rows, cols = len(grid), len(grid[0])
    color_pos = {}
    for i in range(rows):
        for j in range(cols):
            v = grid[i][j]
            if v:
                color_pos.setdefault(v, []).append((i, j))
    segments = []
    blobs = []
    for c, poses in color_pos.items():
        if len(poses) >= 3:
            rs = {r for r, _ in poses}
            cs = {c2 for _, c2 in poses}
            if len(rs) == 1 or len(cs) == 1:
                segments.append((c, poses))
                continue
        blobs.append((c, poses))
    segments.sort(key=lambda x: len(x[1]), reverse=True)
    frame_colors = [c for c, _ in segments]
    blob_color, blob_poses = (blobs[0] if blobs else (None, []))
    if blob_poses:
        rs = [r for r, _ in blob_poses]
        cs = [c2 for _, c2 in blob_poses]
        minr, maxr, minc, maxc = min(rs), max(rs), min(cs), max(cs)
        h_blk = maxr - minr + 1
        w_blk = maxc - minc + 1
    else:
        h_blk = w_blk = 0
    n = max(h_blk, w_blk) + 2 * len(frame_colors)
    out = [[0] * n for _ in range(n)]
    for idx, color in enumerate(frame_colors):
        lo = idx
        hi = n - 1 - idx
        for j in range(lo, hi + 1):
            out[lo][j] = color
            out[hi][j] = color
        for i in range(lo, hi + 1):
            out[i][lo] = color
            out[i][hi] = color
    if blob_color is not None:
        top = (n - h_blk) // 2
        left = (n - w_blk) // 2
        for dr in range(h_blk):
            for dc in range(w_blk):
                out[top + dr][left + dc] = blob_color
    return out