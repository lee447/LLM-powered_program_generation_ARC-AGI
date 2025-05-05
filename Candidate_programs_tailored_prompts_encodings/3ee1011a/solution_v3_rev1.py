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
    for color, poses in color_pos.items():
        if len(poses) >= 3:
            rs = {r for r, _ in poses}
            cs = {c for _, c in poses}
            if len(rs) == 1 or len(cs) == 1:
                segments.append((color, poses))
                continue
        blobs.append((color, poses))
    segments.sort(key=lambda x: len(x[1]), reverse=True)
    frame_colors = [c for c, _ in segments]
    blob_color, blob_poses = (blobs[0] if blobs else (None, []))
    if blob_poses:
        rs = [r for r, _ in blob_poses]
        cs = [c for _, c in blob_poses]
        h_blk = max(rs) - min(rs) + 1
        w_blk = max(cs) - min(cs) + 1
    else:
        h_blk = w_blk = 0
    k = max(h_blk, w_blk)
    n = k + 2 * len(frame_colors)
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
    if blob_color is not None and k > 0:
        top = (n - k) // 2
        left = (n - k) // 2
        for dr in range(k):
            for dc in range(k):
                out[top + dr][left + dc] = blob_color
    return out